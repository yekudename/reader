<template>
    <ul :class="classes" :style="styles"><slot></slot></ul>
</template>
<script>
import {
  oneOf,
  findComponentsDownward,
  findBrothersComponents
} from 'common/utils/assist'
import Emitter from 'common/mixins/emitter'

const prefixCls = 'menu'

export default {
  name: 'Menu',
  mixins: [Emitter],
  props: {
    mode: {
      validator(value) {
        return oneOf(value, ['horizontal', 'vertical'])
      },
      default: 'vertical'
    },
    theme: {
      validator(value) {
        return oneOf(value, ['light', 'dark', 'primary'])
      },
      default: 'light'
    },
    activeName: {
      type: [String, Number]
    },
    openNames: {
      type: Array,
      default() {
        return []
      }
    },
    accordion: {
      type: Boolean,
      default: false
    },
    width: {
      type: String,
      default: '240px'
    }
  },
  data() {
    return {
      currentActiveName: this.activeName,
      openedNames: []
    }
  },
  computed: {
    classes() {
      let theme = this.theme
      if (this.mode === 'vertical' && this.theme === 'primary') theme = 'light'

      return [
        `${prefixCls}`,
        `${prefixCls}-${theme}`,
        {
          [`${prefixCls}-${this.mode}`]: this.mode
        }
      ]
    },
    styles() {
      let style = {}

      if (this.mode === 'vertical') style.width = this.width

      return style
    }
  },
  methods: {
    updateActiveName() {
      if (this.currentActiveName === undefined) {
        this.currentActiveName = -1
      }
      this.broadcast('Submenu', 'on-update-active-name', false)
      this.broadcast(
        'MenuItem',
        'on-update-active-name',
        this.currentActiveName
      )
    },
    updateOpenKeys(name) {
      let names = [...this.openedNames]
      const index = names.indexOf(name)
      if (index >= 0) {
        names.splice(index, 1)
      } else {
        if (this.accordion) {
          let currentSubmenu = null
          findComponentsDownward(this, 'Submenu').forEach(item => {
            if (item.name === name) currentSubmenu = item
          })
          findBrothersComponents(currentSubmenu, 'Submenu').forEach(item => {
            let i = names.indexOf(item.name)
            if (i >= 0) names.splice(i, 1)
          })
          names.push(name)
        }
      }
      this.openedNames = names
      this.$emit('on-open-change', this.openedNames)
    },
    updateOpened() {
      const items = findComponentsDownward(this, 'Submenu')

      if (items.length) {
        items.forEach(item => {
          if (this.openedNames.indexOf(item.name) > -1) item.opened = true
          else item.opened = false
        })
      }
    }
  },
  mounted() {
    this.updateActiveName()
    this.openedNames = [...this.openNames]
    this.updateOpened()
    this.$on('on-menu-item-select', name => {
      this.currentActiveName = name
      this.$emit('on-select', name)
    })
  },
  watch: {
    openNames(names) {
      this.openedNames = names
    },
    activeName(val) {
      this.currentActiveName = val
    },
    currentActiveName() {
      this.updateActiveName()
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import '~common/stylus/variable'
  .menu
    display: block
    margin: 0
    padding: 0
    outline: none
    list-style: none
    color: $color-grey
    font-size: $fontsize-medium
    position: relative
    z-index: 10
  .menu-horizontal
    height: 30px
    line-height: 30px
    .menu-light
      &::after
        content: ''
        display: block
        width: 100%
        height: 1px
        background: $color-grey
        position: absolute
        bottom: 0
        left: 0
  .menu-vertical
    .menu-light
      &::after
        content: ''
        display: block
        width: 1px
        height: 100%
        background: $color-grey
        position: absolute
        top: 0
        right: 0
        z-index: 1
  .menu-light
    background: $color-white
  .menu-dark
    background: $color-drak
  .menu-primary
    background: $color-primary
</style>