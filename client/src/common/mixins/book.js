import {mapMutations, mapGetters} from 'vuex'

export default {
  computed: {
    ...mapGetters([
      'book'
    ])
  },
  methods: {
    ...mapMutations({
      setBook: 'SET_BOOK'
    }),
    updateBook(index) {
      let b = this.book
      b.curChapter = index
      b.nextChapter = ((index + 1) < b.chapters.length) ? index + 1 : null
      b.prevChapter = ((index - 1) >= 0) ? index - 1 : null
      this.setBook(b)
    },
    getNextChapter(chapter) {
      let index = this.book.chapters.indexOf(chapter)
      if (index === -1) {
        return null
      } else if (index >= this.book.chapters.length - 1) {
        return null
      } else {
        return this.book.chapters[++index]
      }
    },
    getPrevChapter(chapter) {
      let index = this.book.chapters.indexOf(chapter)
      if (index === -1) {
        return null
      } else if (index <= 0) {
        return null
      } else {
        return this.book.chapters[--index]
      }
    },
    findIndex(id, list) {
      return list.findIndex((item) => {
        return item.id === id
      })
    }
  }
}