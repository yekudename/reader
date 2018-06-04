<template>
  <li class="comment-item border-bottom-1px" @click="selectItem">
    <slot>
      <div class="comment-user">
        <img :src="item.user.avatar">
        <div class="comment-user-name">{{item.user.name}}</div>
      </div>
      <div class="comment-text">{{item.text}}</div>
      <div class="comment-foot">
        <div class="comment-time">{{item.time}}</div>
        <div class="comment-response"><i class="fa fa-commenting-o"></i>&nbsp;{{item.response}}</div>
      </div>
    </slot>
  </li>
</template>

<script type="text/ecmascript-6">
const COMPONENT_NAME = 'comment-item'
const EVENT_SELECT = 'select'

export default {
  name: COMPONENT_NAME,
  props: {
    item: Object,
  },
  create() {
    console.log(this.item)
  },
  computed: {
    updateTime() {
      return (new Date() - new Date(this.time))
    }
  },
  methods: {
    selectItem() {
      this.$emit(EVENT_SELECT, this.item)
    }
  }
}
</script>

<style lang="stylus">
  @import '~common/stylus/variable'
  .comment-item
    padding: 10px 0
  .comment-user
    display: flex
    align-items: center
    & img
      width: 30px
      height: 30px
      border-radius: 50%
    .comment-user-name
      padding-left: 10px
      font-size: $fontsize-medium
      color: $color-title

  .comment-text
    padding-left: 40px
    height: 40px
    line-height: 20px
    overflow: hidden
    font-size: $fontsize-medium
    color: $color-text

  .comment-foot
    padding-left: 40px
    display: flex
    justify-content: space-between
    .comment-time,.comment-response
      padding-top: 5px
      font-size: $fontsize-small
      color: $color-text
</style>

