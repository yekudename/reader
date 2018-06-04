<template>
  <div class="bookshelf">
    <scroll :options="options">
      <book-item @select="selectBook" v-for="(item, index) in bookshelf" :item="item" :key="index"></book-item>
    </scroll>
    <router-view></router-view>
  </div>
</template>

<script>
import Scroll from 'base/scroll/scroll'
import IndexListItem from 'base/index-list/index-list-item'
import BookItem from 'components/books-group/book-item'
import {bookList} from 'api/getdata'
import Book from 'common/js/book'
import {mapMutations} from 'vuex'

export default {
  name: 'bookshelf',
  data() {
    return {
      bookshelf: []
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
  created() {
    this._getBookshelf()
  },
  methods: {
    async _getBookshelf() {
      let books = await bookList()
      this.bookshelf = books.novels
    },
    selectBook (book) {
      this.$router.push({
        path: `/book/${book.id}`
      })
      this.setBook(new Book({
        id: book.id,
        name: book.name,
        author: book.author,
        description: book.description,
        image: book.img,
        url: book.url,
        category: book.category,
        keywords: book.keywords,
        updateTime: book.updateTime,
        state: book.state,
        chapters: book.chapters
      }))
    },
    ...mapMutations ({
      setBook: 'SET_BOOK'
    })
  },
  components: {
    Scroll,
    IndexListItem,
    BookItem
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "~common/stylus/variable"

  .bookshelf
    height: 100%
    width: 100%
    overflow: hidden
</style>
