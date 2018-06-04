<template>
  <div class="feature">
    <scroll :data="booksGroup" :options="options">
      <div ref="slideWrapper" class="slide-container">
        <slide
        ref="slide"
        :data="booksSlide"
        :initial-index="initialIndex"
        :loop="loop"
        :auto-play="autoPlay"
        :interval="interval"
        :threshold="threshold"
        :speed="speed"
        :allow-vertical="allowVertical">
          <slide-item v-for="(item, index) in booksSlide" :key="index" :item="item" class="book-slide">
          </slide-item>
        </slide>
      </div>
      <div>
        <button-group>
          <c-button :light="true">排行</c-button>
          <c-button :light="true">分类</c-button>
          <c-button :light="true">专题</c-button>
        </button-group>
      </div>
      <books-group v-for="(group, index) in booksGroup" :group="group" :key="index" class="book-group" @select="selectItem"></books-group>
    </scroll>
  </div>
</template>

<script type="text/ecmascript-6">
import Scroll from 'base/scroll/scroll'
import Slide from 'base/slide/slide'
import SlideItem from 'base/slide/slide-item'
import BooksGroup from 'components/books-group/books-group'
import BookItem from 'components/books-group/book-item'
import ButtonGroup from 'components/button-group/button-group'
import CButton from 'base/button/button'
import {getBooksGroup, getBookshelf} from 'api/bookshelf'

export default {
  components: {
    Scroll,
    BooksGroup,
    BookItem,
    Slide,
    SlideItem,
    ButtonGroup,
    CButton
  },
  data() {
    return {
      loop: true,
      autoPlay: true,
      interval: 4000,
      threshold: 0.3,
      speed: 400,
      allowVertical: false,
      initialIndex: 1,
      dotsSlot: false,
      addItem3: false,
      booksSlide: [],
      booksGroup: []
    }
  },
  computed: {
    options() {
      return {
        probeType: 3,
        pullDownRefresh: this.pullDownRefresh,
        pullUpLoad: this.pullUpLoad,
        mouseWheel: {
          speed: 20,
          invert: false
        }
      }
    }
  },
  created() {
    this._getBooksGroup()
    this._getBooksSlide()
  },
  methods: {
    selectItem(item) {
      console.log(item.name)
    },
    clickTitle(title) {
      console.log(title)
    },
    _getBooksGroup() {
      getBooksGroup().then((res) => {
        if (res.errno === 0) {
          this.booksGroup = res.data
        }
      })
    },
    _getBooksSlide() {
      getBookshelf().then((res) => {
        if (res.errno === 0) {
          this.booksSlide = res.data.data
        }
      })
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .feature
    width: 100%
    height: 100%
    overflow: hidden
    .slide-container
      height: 200px
      margin-bottom: 15px
      transform: translateZ(0px)
      overflow: hidden
</style>