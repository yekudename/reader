<template>
  <ul class="comment">
    <slot name="title">
      <div class="comment-title">
        <div class="comment-title-text" v-text="title"></div>
        <div class="comment-title-more">
          <span>更多</span>
          <i class="fa fa-angle-right"></i>
        </div>
      </div>
    </slot>
    <slot>
      <comment-item v-for="(item, index) in items" :key="index" :item="item" @select="handleSelect"></comment-item>
    </slot>
  </ul>
</template>

<script>
import CommentItem from './comment-item'

export default {
  props: {
    title: {
      type: String,
      default: "评论"
    },
    items: [Object, Array]
  },
  methods: {
    handleSelect(item) {
      this.$emit('select', item)
    }
  },
  components: {
    CommentItem
  }
}
</script>


<style lang="stylus">
  @import '~common/stylus/variable'

  .comment
    padding: 10px
    .comment-title
      display: flex
      justify-content: space-between
    .comment-title-text
      font-size: $fontsize-large
    .comment-title-more span
      font-size: $fontsize-small
      color: $color-title
</style>

