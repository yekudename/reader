<template>
  <div class="discover">
    <scroll
      ref="scroll"
      :options="options"
      :data="optionItems">
      <div class="option-list-content" ref="content">
        <ul>
          <cell
            v-for="(item, index) in optionItems"
            :key="index"
            :title="item.title"
            iconRight="angle-right"
            is-link
            :to="item.routerLink"
            class="border-bottom-1px"
            @select="selectItem">
          </cell>
        </ul>
      </div>
    </scroll>
  </div>
</template>

<script type="text/ecmascript-6">

import Scroll from 'base/scroll/scroll.vue'
import Cell from 'components/cell/cell'

const COMPONENT_NAME = 'discover'

export default {
  name: COMPONENT_NAME,
  data() {
    return {
      optionItems: [
        {
          icon: 'music',
          title: '分类',
          routerLink: '/category'
        },
        {
          icon: 'music',
          title: '排行榜',
          routerLink: '/rank'
        },
        {
          icon: 'music',
          title: '主题书单',
          routerLink: '/booklist'
        },
        {
          icon: 'music',
          title: '精品专区',
          routerLink: '/category'
        },
        {
          icon: 'music',
          title: '今日免费',
          routerLink: '/category'
        }
      ]
    }
  },
  computed: {
    options() {
      return {
        probeType: 3,
        pullDownRefresh: this.pullDownRefresh,
        pullUpLoad: this.pullUpLoad,
        mouseWheel: true
      }
    }
  },
  methods: {
    selectItem(item) {
      console.log(this.optionItems.indexOf(item) + 1 + '.' + item.title)
      this.$router.push(item.routerLink)
    }
  },
  components: {
    Scroll,
    Cell
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @require "~common/stylus/variable.styl"
  @require "~common/stylus/mixin.styl"

  .discover
    width: 100%
    height: 100%
    overflow: hidden
    color: $color-grey
    background-color: $color-background
    .option-list-content
      border-radius: 2px
</style>
