<template>
  <li
    class="book-item border-bottom-1px"
    :class="itemClass"
    @click="selectItem()">
    <slot>
      <div class="book-list-item-def">
        <div class="item-image">
          <img :src="item.img" v-if="item.img">
        </div>
        <div class="item-info">
          <h4 class="item-info-title">{{item.name}}</h4>
          <div class="item-info-content" v-if="item.author">
            <div class="item-info-author">{{item.author}}</div>
            <div class="item-info-category">{{item.category}}</div>
            <div class="item-info-state">{{item.state}}</div>
            <div class="item-info-word-count">{{item.word_count}}</div>
          </div>
          <div class="item-info-desc" v-if="item.description">{{item.description}}</div>
        </div>
      </div>
    </slot>
  </li>
</template>

<script type="text/ecmascript-6">
import {
  addClass,
  removeClass
} from 'common/helpers/dom'
import ButtonGroup from 'components/button-group/button-group'
import CButton from 'base/button/button'

const COMPONENT_NAME = 'book-item'
const ACTIVE_CLS = 'book-list-item_active'
const EVENT_SELECT = 'select'

export default {
  name: COMPONENT_NAME,
  components: {
    ButtonGroup,
    CButton
  },
  props: {
    item: {
      type: Object,
      default() {
        return {}
      }
    }
  },
  create() {
    console.log(this.item)
  },
  computed: {
    itemClass() {
      return this.item.active ? ACTIVE_CLS : ''
    },
    updateTime() {
      return (new Date() - new Date(this.item.updateTime))
    }
  },
  methods: {
    selectItem() {
      this.$emit(EVENT_SELECT, this.item)
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @require "~common/stylus/variable.styl"
  @require "~common/stylus/mixin.styl"
  .book-item
    padding: 10px
  .book-list-item-def
    display: flex
    height: 80px
    margin: 0
    border-bottom: $$color-light-grey solid 1px
    .item-image
      width: 60px
      & img
        width: 60px
        height: 80px
        border-radius: 2px
    .item-info
      margin-left: 10px
      padding-top: 5px
      color: $index-list-anchor-color
      .item-info-title
        font-size: $fontsize-medium
      .item-info-desc
        height: 34px
        line-height: 17px
        overflow: hidden
        text-overflow: ellipsis
        padding-top: 5px
        font-size: $fontsize-small
      .item-info-content
        display: flex
        padding-top: 5px
        font-size: $fontsize-small
        .item-info-category,.item-info-state,.item-info-word-count
          padding-left: 5px
        .item-info-continue
          margin-left: 5px
</style>
