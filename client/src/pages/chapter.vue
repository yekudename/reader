<template>
  <page class="chapter" title="目录">
    <scroll slot="content">
      <cell
        @select="updateBook(index)"
        v-for="(chapter, index) in chapters"
        :key="index"
        :title="chapter.title"
        class="chapter-item border-bottom-1px"
        :to="{path:'/book/chapter/' + chapter.id}"
      ></cell>
    </scroll>
  </page>
</template>
<script>
import Cell from 'components/cell/cell'
import Scroll from 'base/scroll/scroll'
import Page from 'components/page-template/page-template'
import {chapter} from 'api/getdata'
import {mapMutations, mapGetters} from 'vuex'
import bookMixin from 'common/mixins/book'

export default {
  mixins: [bookMixin],
  data() {
    return {
      chapters: null
    }
  },
  computed: {
    ...mapGetters([
      'book'
    ])
  },
  created() {
    this.getBookChapterById(this.book.id)
  },
  methods: {
    async getBookChapterById(id) {
      if (!id) {
        return
      }
      let c = await chapter(id)
      this.chapters = c.chapters
    }
  },
  components: {
    Cell,
    Scroll,
    Page
  }
}
</script>

<style lang="stylus">
  @import '~common/stylus/variable'

  .chapter
    position: fixed
    top: 0
    left: 0 
    width: 100%
    height: 100%
    z-index: 20
    background yellow
    .chapter-item
      background-color: $color-white
</style>

