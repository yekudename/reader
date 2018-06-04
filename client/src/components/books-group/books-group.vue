<template>
  <li class="book-group">
    <div class="book-list-title">
      <section class="book-list-anchor">{{group.name}}</section>
      <section class="book-list-more">更多 ></section>
    </div>
    <ul>
      <slot>
        <book-item v-for="(item, index) in group.items" :key="index" :item="item" @select="selectItem"></book-item>
      </slot>
    </ul>
  </li>
</template>

<script>
import BookItem from './book-item'
const EVENT_SELECT = 'select'

export default {
  name: 'booksgroup',
  props: {
    group: {
      type: Object,
      default() {
        return {}
      }
    }
  },
  methods: {
    selectItem(item) {
      this.$emit(EVENT_SELECT, item)
    }
  },
  components: {
    BookItem
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import '~common/stylus/variable'

  .book-list-title
    position: relative
    width: 100%
    height: 2rem
    .book-list-anchor
      left: 0.4rem
      height: 1rem
      line-height: 2.2rem
      margin-left: .4rem
    .book-list-more
      position: absolute
      top: 50%
      transform: translateY(-50%)
      right: 0.55rem
      color: $color-grey
      font-size: $fontsize-small-s
</style>
