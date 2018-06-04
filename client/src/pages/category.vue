<template>
  <page-template title="分类">
    <div slot="content" class="category">
      <scroll :options="options" :data="categorys">
        <div class="category-content" v-for="(cates, index) in categorys" :key="index" ref="bookgroups">
          <h3 class="category-male-title">{{cates.group}}<span class="book-count">(共{{bookCount}}部)</span></h3>
          <div class="category-male-content">
            <cell-block
              v-for="(cate, index) in cates.category"
              :title="cate.title"
              :img="cate.img"
              :info="cate.bookCount"
              :key="index">
            </cell-block>
          </div>
        </div>
      </scroll>
    </div>
  </page-template>
</template>

<script>
import PageTemplate from 'components/page-template/page-template'
import CellBlock from 'components/cell/cell-block'
import Scroll from 'base/scroll/scroll'
import {bookCategory} from 'api/getdata'

export default {
  components: {
    PageTemplate,
    CellBlock,
    Scroll
  },
  data() {
    return {
      categorys: []
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
    bookCount() {
      return this.allCount(this.categorys[0].category)
    }
  },
  created() {
    this.initData()
  },
  methods: {
    async initData() {
      let c = await bookCategory()
      if (c.errno === 0) {
        this.categorys = c.data
      }
    },
    allCount(data) {
      if (!data) {
        return
      }
      let allCount = 0
      for (let i = 0; i < data.length; i++) {
        allCount += data[i].bookCount
      }
      return allCount
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import '~common/stylus/variable'
  .category
    height: 100%
    overflow: hidden
  .category-content
    margin-left: 10px
    .category-male-content, .category-famale-content
      display: flex
      flex-wrap: wrap
      justify-content: flex-start
    .category-male-title, .category-famale-title
      padding: 10px 0 0 0
      .book-count
        margin-left: 5px
        font-size: $fontsize-small
        color: $color-grey
</style>
