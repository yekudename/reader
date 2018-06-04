<template>
  <page-template>
    <div slot="header" class="search-header">
      <div class="search-header-back" @click="back">
        <i class="fa fa-angle-left fa-lg"></i>
      </div>
      <i-input
        class="search-header-input"
        :clearable="true"
        placeholder="输入书名或作者名"
        v-model="query">
      </i-input>
      <div class="search-header-search">
        <i class="fa fa-search fa-lg"></i>
      </div>
    </div>
    <div slot="content" class="search-result">
      <scroll ref="result" class="search-result-cell">
        <cell
          class="border-bottom-1px"
          @select="selectBook(novel)"
          v-for="(novel, index) in result" :key="index"
          icon="search"
          :title="novel.name"
          :to="'/book/' + novel.id">
        </cell>
      </scroll>
    </div>
  </page-template>
</template>

<script>
import PageTemplate from 'components/page-template/page-template'
import IInput from 'base/input/input'
import Scroll from 'base/scroll/scroll'
import Cell from 'components/cell/cell'
import {search} from 'api/getdata'
import {debounce} from 'common/js/utils'
import BookMixin from 'common/mixins/book'
import Book from 'common/js/book'

const perpage = 20

export default {
  components: {
    PageTemplate,
    IInput,
    Scroll,
    Cell
  },
  mixins: [BookMixin],
  data() {
    return {
      query: '',
      page: 1,
      hasMore: true,
      result: []
    }
  },
  computed: {
  },
  methods: {
    async search(query) {
      this.page = 1
      this.hasMore = true
      this.$refs.result.scrollTo(0, 0)
      let r = await search(query, this.page, perpage)
      this.result = r.novels
      this.hasMore = r.next ? true : false
    },
    back() {
      this.$router.back()
    },
    clear() {
      this.query = ''
    },
    setQuery(query) {
      this.query = query
    },
    selectBook(book) {
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
    }
  },
  created() {
    this.$watch('query', debounce((newQuery) => {
      this.$emit('query-change', newQuery)
    }, 300))
  },
  mounted() {
    this.$on('query-change', (newQuery) => {
      this.search(newQuery)
    })
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import '~common/stylus/variable'

  .search-header
    width: 100%
    display: flex
    align-items: center
    .search-header-back
      width: 32px
      text-align: center
    .search-header-input
      height: 42px
    .search-header-search
      width: 32px
      height: inherit
      text-align: center
      color: $primary-color
</style>
