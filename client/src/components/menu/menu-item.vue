<template>
  <li :class="classes" @click.stop="handleClick" :style="itemStyle"><slot>{{name}}</slot></li>
</template>
<script>
import Emitter from 'common/mixins/emitter'
import { findComponentUpward } from 'common/utils/assist'
import mixin from './mixin'
const prefixCls = 'menu'

export default {
  name: 'MenuItem',
  mixins: [Emitter, mixin],
  props: {
    name: {
      type: [String, Number],
      required: true
    },
    disabled: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      active: false
    }
  },
  computed: {
    classes() {
      return [
        `${prefixCls}-item`,
        {
          [`${prefixCls}-item-active`]: this.active,
          [`${prefixCls}-item-selected`]: this.active,
          [`${prefixCls}-item-disabled`]: this.disabled
        }
      ]
    },
    itemStyle() {
      return this.hasParentSubmenu && this.mode !== 'horizontal'
        ? {paddingLeft: 43 + (this.parentSubmenuNum - 1) * 24 + 'px'}
        : {}
    }
  },
  methods: {
    handleClick() {
      if (this.disabled) return
      let parent = findComponentUpward(this, 'Submenu')
      if (parent) {
        this.dispatch('Submenu', 'on-menu-item-select', this.name)
      } else {
        this.dispatch('CMenu', 'on-menu-item-select', this.name)
      }
    }
  },
  mounted() {
    this.$on('on-update-active-name', name => {
      if (this.name === name) {
        this.active = true
        this.dispatch('Submenu', 'on-update-active-name', name)
      } else {
        this.active = false
      }
    })
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import '~common/stylus/variable'
  .menu-item
    display: block
    outline: none
    list-style: none
    font-size: $fontsize-medium
    position: relative
    z-index: 1
    cursor: pointer
    transition: all .2s ease-in-out
  .menu-item > i
    margin-right: 6px
  .menu-submenu-title > i, .menu-submenu-title span > i
    margin-right: 8px
  .menu-horizontal .menu-item, .menu-horizontal .menu-submenu
    float: left
    padding: 0 20px
    position: relative
    cursor: pointer
    z-index: 3
    transition: all .2s ease-in out
  .menu-light.menu-horizontal .menu-item, .menu-light.menu-horizontal .menu-submenu
    height: inherit
    line-height: inherit
    border-bottom 2px solid transparent
    color: $color-grey
  .menu-item-active, .menu-item:hover
    color: red
    border-bottom: 2px solid $color-orange
</style>
