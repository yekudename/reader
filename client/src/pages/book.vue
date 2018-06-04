<template>
  <page class="book" title="书籍详情" @back="pageBack">
    <scroll slot="content" class="book-content">
      <div class="book-info">
        <div class="book-info-img">
          <img :src="bookData.img">
        </div>
        <div class="book-info-name">{{bookData.name}}</div>
        <div class="book-info-author">
          <span>{{bookData.author}}</span>
          <span>{{bookData.category}}</span>
        </div>
      </div>
      <div class="book-description">
        <p>&emsp;&emsp;{{bookData.description}}</p>
      </div>
      <cell class="book-chapter" :is-link="true" icon-right="angle-right" to="/book/chapter">
        <div slot="title">目录</div>
        <div slot="value" class="book-chapter-last">连载至{{bookData.last_chapter}}&emsp;{{bookData.updatetime}}前更新</div>
      </cell>
      <comment :items="comments" @select="selectComment"></comment>
      <recommend title="同类作品推荐" :recommends="recommends" @select="selectRecommendBook"></recommend>
      <div class="fixed-place"></div>
    </scroll>
    <div slot="footer" class="book-action-group">
      <c-button type="text" size="large">批量下载</c-button>
      <c-button type="primary" size="large" @click="startRead">开始阅读</c-button>
      <c-button type="text" size="large">{{inBookShelf ? "已在书架" : "加入书架"}}</c-button>
    </div>
    <router-view></router-view>
  </page>
</template>

<script>
import Page from 'components/page-template/page-template'
import Scroll from 'base/scroll/scroll'
import BookItem from 'components/books-group/book-item'
import ButtonGroup from 'components/button-group/button-group'
import CButton from 'base/button/button'
import Cell from 'components/cell/cell'
import Comment from 'components/comment/list'
import Recommend from 'components/recommend/recommend'
import BookMixin from 'common/mixins/book'
import {book} from 'api/getdata'
import {mapGetters} from 'vuex'

export default {
  mixins: [BookMixin],
  data() {
    return {
      inBookShelf: false,
      bookData: {},
      comments: [
        {
          user: {
            avatar: '/static/img/book10001.jpg',
            name: '任意XX'
          },
          text: '看个病看一天，发哦iahfjlkajflakfasfafiwnalskfm;alsfl;ahfuwnad;lv;amvaml加哦案例覅骄傲爱妃就怕骄傲放假啊爱就爱；是根据公司是考四六级改革十几个',
          time: '今天 9:39',
          response: '126'
        },
        {
          user: {
            avatar: '/static/img/book10001.jpg',
            name: '任意XX'
          },
          text: '看个病看一天，发哦i加哦案例覅骄傲爱妃就怕骄傲放假啊爱就爱；是根据公司是考四六级改革十几个',
          time: '今天 9:39',
          response: '6'
        },
        {
          user: {
            avatar: '/static/img/book10001.jpg',
            name: '任意XX'
          },
          text: '看个病看一天，发哦i加哦案例覅骄傲爱妃就怕骄傲放假啊爱就爱；是根据公司是考四六级改革十几个',
          time: '今天 9:39',
          response: '6'
        }
      ],
      recommends: [
        {
          img: '/static/img/book10001.jpg',
          name: '任意XX'
        },
        {
          img: '/static/img/book10001.jpg',
          name: '任意XX任意XX任意XX任意XX任意XX'
        },
        {
          img: '/static/img/book10001.jpg',
          name: '任意XahlafiksssssssssssssX这'
        },
        {
          img: '/static/img/book10001.jpg',
          name: 'jaffkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'
        }
      ]
    }
  },
  components: {
    Page,
    BookItem,
    ButtonGroup,
    CButton,
    Cell,
    Comment,
    Scroll,
    Recommend
  },
  computed: {
    ...mapGetters([
      'book'
    ])
  },
  created() {
    this.initData()
  },
  methods: {
    async initData() {
      if(!this.book.id) {
        this.$router.push('/')
        return
      }
      this.bookData = await book(this.book.id)
    },
    selectComment(item) {
      console.log(item)
    },
    selectRecommendBook(item) {
      console.log(item)
    },
    pageBack() {
      this.$router.push('/home/bookshelf')
    },
    startRead() {
      let chapterid = this.book.curChapter ? this.book.chapters[this.book.curChapter].id : this.book.chapters[0].id
      let index = this.findIndex(chapterid, this.book.chapters)
      if (index > -1) {
        this.updateBook(index)
      }
      this.$router.push('/book/chapter/' + chapterid)
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "~common/stylus/variable"

  .book-content
    .book-info
      display: flex
      flex-direction: column
      padding: 20px 0 10px 0
      background: $color-primary
      .book-info-img, .book-info-author, .book-info-name
        align-self: center
      .book-info-img img
        width: 80px
        height: 100px
      .book-info-name
        line-height: 20px
        color: $color-white
      .book-info-author
        color: $color-white
        font-size: $fontsize-small
    .book-description
      padding: 10px 5px
      & p
        line-height: 20px
        color: $color-grey
        font-size: $fontsize-medium
    .book-chapter
      .book-chapter-last
        font-size: $fontsize-small
        color: $color-text

  .book-action-group
    position: fixed
    width: 100%
    bottom: 0
    left: 0
    background-color: white
    z-index: 10
    display: flex
    & button
      flex: 1
      border-radius : 0

  .fixed-place
    height: 36px
</style>


