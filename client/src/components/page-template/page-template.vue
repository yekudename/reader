<template>
  <div class="page" :class="type">
    <header class="header">
      <slot name="header">
        <div class="header-back" @click="back">
          <i class="fa fa-angle-left fa-lg"></i>
        </div>
        <div class="header-title">{{title}}</div>
      </slot>
    </header>
    <div class="wrapper">
      <section v-show="desc" class="desc">
        <slot name="desc">{{desc}}</slot>
      </section>
      <div class="page-wrapper-content">
        <slot name="content">{{content}}</slot>
      </div>
    </div>
    <slot name="footer"></slot>
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'page-template',
  props: {
    type: {
      type: String,
      default: ''
    },
    title: {
      type: String,
      default: ''
    },
    desc: {
      type: String,
      default: ''
    },
    content: {
      type: String,
      default: ''
    }
  },
  methods: {
    back() {
      this.$router.back()
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "~common/stylus/variable"

  .page
    width: 100%
    height: 100%
    transform: translateZ(0)
    .header
      position: relative
      display: flex
      align-items: center
      height: 44px
      line-height: 44px
      background-color: #edf0f4
      -webkit-backface-visibility: hidden
      backface-visibility: hidden
      .header-back
        width: 32px
        text-align: center
      .header-title
        font-size: $fontsize-large
        text-align: left
        padding-left: 10px
        width: 100%
      .icon-back
        text-align: left
        font-size: 20px
        padding-top: 12px
        color: #fc9153
        margin-left: 10px
    >.wrapper
      height: calc(100% - 44px)
      background-color: $color-white
      overflow: auto
      -webkit-overflow-scrolling: touch
      .desc
        padding: 10px
        margin: 10px 0
        line-height: 20px
        font-size: 14px
      .page-wrapper-content
        width: 100%
        height: 100%
        overflow: hidden
</style>
