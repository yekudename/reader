<template>
  <div class="cell-block">
    <slot>
      <section class="cell-block-left">
        <img class="cell-block-img" :class="img" :src="img" v-if="img">
      </section>
      <section class="cell-block-right">
        <div class="cell-block-title">{{title}}</div>
        <div class="cell-block-info">{{info}}</div>
      </section>
    </slot>
  </div>
</template>

<script>

export default {
  props: {
    img: {
      type: String,
      default: ''
    },
    title: {
      type: String,
      default: ''
    },
    info: {
      type: [String, Number, Object],
      default: ''
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import '~common/stylus/variable'
  @import '~common/stylus/mixin'
  .cell-block
    display: flex
    height: 100px
    width: 45%
    margin: 10px 10px 0 0
    font-size: $fontsize-medium
    .cell-block-img
      width: 80px
      height: 100px
    .cell-block-right
      margin-left: 10px
      padding: 30px 0 0 0
      .cell-block-title
        font-size: $fontsize-medium
      .cell-block-info
        margin-top: 10px
        font-size: $fontsize-small
        color: $color-grey
</style>