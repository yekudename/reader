<template>
  <a class="cell" :href="href">
    <span class="cell-mask" v-if="isLink"></span>
    <div class="cell-left">
      <slot name="left"></slot>
    </div>
    <div class="cell-wrapper">
      <div class="cell-title">
        <slot name="icon">
          <i v-if="icon" class="mintui" :class="'fa fa-' + icon"></i>
        </slot>
        <slot name="title">
          <span class="cell-text" v-text="title"></span>
          <span v-if="label" class="cell-label" v-text="label"></span>
        </slot>
      </div>
      <div class="cell-value" :class="{ 'is-link' : isLink }">
        <slot name="value">
          <span v-text="value"></span>
        </slot>
      </div>
      <i v-if="isLink" class="cell-allow-right" :class="'fa fa-' + iconRight"></i>
    </div>
    <div class="cell-right">
      <slot name="right"></slot>
    </div>
  </a>
</template>

<script>
/**
 * mt-cell
 * @module components/cell
 * @desc 单元格
 * @param {string|Object} [to] - 跳转链接，使用 vue-router 的情况下 to 会传递给 router.push，否则作为 a 标签的 href 属性处理
 * @param {string} [icon] - 图标，提供 more, back，或者自定义的图标（传入不带前缀的图标类名，最后拼接成 .mintui-xxx）
 * @param {string} [title] - 标题
 * @param {string} [label] - 备注信息
 * @param {boolean} [is-link=false] - 可点击的链接
 * @param {string} [value] - 右侧显示文字
 * @param {slot} - 同 value, 会覆盖 value 属性
 * @param {slot} [title] - 同 title, 会覆盖 title 属性
 * @param {slot} [icon] - 同 icon, 会覆盖 icon 属性，例如可以传入图片
 *
 * @example
 * <cell title="标题文字" icon="back" is-link value="描述文字"></cell>
 * <cell title="标题文字" icon="back">
 *   <div slot="value">描述文字啊哈</div>
 * </cell>
 */
export default {
  name: 'cell',

  props: {
    to: [String, Object],
    icon: String,
    title: String,
    label: String,
    isLink: Boolean,
    value: {},
    iconRight: String
  },

  computed: {
    href() {
      if (this.to && !this.added && this.$router) {
        const resolved = this.$router.match(this.to)
        if (!resolved.matched.length) return this.to

        this.$nextTick(() => {
          this.added = true
          this.$el.addEventListener('click', this.handleClick)
        })
        return resolved.fullPath || resolved.path
      }
      return this.to
    }
  },

  methods: {
    handleClick($event) {
      $event.preventDefault()
      this.$emit('select')
      this.$router.push(this.href)
    }
  }
}
</script>

<style lang="stylus">
  @import '~common/stylus/variable'
  .cell
    background-color: $color-white
    box-sizing: border-box
    color: inherit
    min-height: 40px
    display: block
    overflow: hidden
    position: relative
    text-decoration: none

    .cell-wrapper
      display: flex
      align-items: center
      font-size: $fontsize-medium
      line-height: 1
      min-height: inherit
      overflow: hidden
      padding: 0 10px
      width: 100%

      .cell-text
        vertical-align: middle

      .cell-label
        color: $color-grey
        display: block
        font-size: $fontsize-small
        margin-top: 6px

      .cell-title
        flex: 1

      .cell-value
        color: $color-grey
        display: flex
        align-items: center
        margin-right: 34px

    .cell-left
      position: absolute
      height: 100%
      left: 0
      transform: translate3d(-100%, 0, 0)

    .cell-right
      position: absolute
      height: 100%
      right: 0
      top: 0
      transform: translate3d(100%, 0, 0)

    .cell-allow-right
      position: absolute
      top: 50%
      right: 10px
      size: 5px
      transform: translateY(-50%)
</style>
