<template>
  <page-template title="排行">
    <div slot="content" class="rank">
      <div class="left-sidebar">
        <div class="side-menu border-bottom-1px" v-for="(menu, index) in sidebar" :key="index" @click="handleClick(menu)">{{menu.title}}</div>
      </div>
      <div class="right-content">
        <h3 class="content-title">title</h3>
        <scroll :options="options" :data="rank" class="content-scroll">
          <book-item v-for="(book, index) in rank" :item="book" :key="index"></book-item>
        </scroll>
      </div>
    </div>
  </page-template>
</template>

<script>
import PageTemplate from 'components/page-template/page-template'
import CellBlock from 'components/cell/cell-block'
import Scroll from 'base/scroll/scroll'
import BookItem from 'components/books-group/book-item'
import {rankBookList} from 'api/getdata'

export default {
  components: {
    PageTemplate,
    CellBlock,
    Scroll,
    BookItem
  },
  data() {
    return {
      sidebar: [
        {
          title: '点击榜',
          rankid: 1
        },
        {
          title: '畅销榜',
          rankid: 2
        },
        {
          title: '月票榜',
          rankid: 3
        },
        {
          title: '推荐榜',
          rankid: 4
        },
        {
          title: '打赏榜',
          rankid: 5
        },
        {
          title: '更新榜',
          rankid: 6
        },
        {
          title: '签约榜',
          rankid: 7
        },
        {
          title: '新书榜',
          rankid: 8
        },
        {
          title: '新人榜',
          rankid: 9
        },
        {
          title: '红包榜',
          rankid: 10
        },
        {
          title: '书单榜',
          rankid: 11
        }
      ],
      booksData: [
        {
          image: 'static/image/book10001.jpg',
          name: '古代言情',
          bookCount: 284771
        },
        {
          image: 'static/image/book10002.jpg',
          name: '现代言情',
          bookCount: 284771
        },
        {
          image: 'static/image/book10003.jpg',
          name: '玄幻言情',
          bookCount: 284771
        },
        {
          image: 'static/image/book10004.jpg',
          name: '悬疑灵异',
          bookCount: 284771
        },
        {
          image: 'static/image/book10005.jpg',
          name: '浪漫青春',
          bookCount: 284771
        },
        {
          image: 'static/image/book10006.jpg',
          name: '仙侠奇缘',
          bookCount: 284771
        },
        {
          image: 'static/image/book10007.jpg',
          name: '科幻空间',
          bookCount: 284771
        },
        {
          image: 'static/image/book10008.jpg',
          name: '游戏竞技',
          bookCount: 284771
        },
        {
          image: 'static/image/book10009.jpg',
          name: 'N次元',
          bookCount: 284771
        }
      ],
      rank: []
    }
  },
  computed: {
    options() {
      return {
        probeType: 3,
        mouseWheel: {
          speed: 20,
          invert: false
        }
      }
    },
    maleBookCount() {
      return this.allCount(this.maleData)
    },
    famaleBookCount() {
      return this.allCount(this.famaleData)
    }
  },
  created() {
    this.initData(1, '12')
  },
  methods: {
    async initData(rankid, offset) {
      let id = rankid || 1
      let o = offset || 20
      let c = await rankBookList(id, o)
      if (c.errno === 0) {
        this.rank = c.data
        console.log(this.rank)
      }
    },
    allCount(data) {
      if (!data) {
        return
      }
      let allCount = 0
      for (let i = 0; i < data.length; i++) {
        allCount += this.maleData[i].bookCount
      }
      return allCount
    },
    handleClick(item) {
      console.log(item.rankid)
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import '~common/stylus/variable'
  .rank
    height: 100%
    display: flex
    .left-sidebar
      width: 25%
      height: 100%
      .side-menu
        padding: 10px 0 10px 0
        font-size: $fontsize-medium
        text-align: center
        .side-menu:active
          border-left: 2px solid red
          background blue
    .right-content
      width: 75%
      height: 100%
      overflow: hidden
      .content-title
        padding: 10px
        font-size: $fontsize-medium
      .content-scroll
        height: calc(100% - 34px)
</style>
