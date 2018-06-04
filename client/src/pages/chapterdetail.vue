<template>
  <div class="chapter-detail">
    <index-list
      ref="scroll"
      :data="chapters"
      :pullUpLoad="options.pullUpLoad"
      :pullDownRefresh="options.pullDownRefresh"
      :navbar="false"
      @pulling-down="onPullingDown"
      @pulling-up="onPullingUp"
      @current-index-changed="getCurrentIndex">
      <li
        class="chapter-detail-item index-list-group"
        v-for="(chapter, index) in chapters"
        :key="index"
        :style="textStyle"
        @click="showModal">
        <div class="chapter-detail-title" ref="title">{{chapter.title}}</div>
        <p v-html="chapter.text" class="chapter-detail-text"></p>
      </li>
    </index-list>
    <modal v-model="modal3" position="bottom" class="modal-menu-bottom" width="100" :footer-hide="true" :closable="false" :mask-hidden="true">
      <div class="modal-bottom-content">
        <span @click="showChapter"><i class="fa fa-list-ul"> 目录</i></span>
        <span @click="changeMode"><i :class="'fa fa-' + iconMode"> {{iconText}}</i></span>
        <span @click="showSetting"><i class="fa fa-font"> 设置</i></span>
      </div>
    </modal>
    <modal v-model="modal2" position="top" class="modal-menu-top" width="100" :footer-hide="true" :closable="false" :mask-hidden="true">
      <div class="modal-top-content">
        <span class="back"><i class="fa fa-angle-left fa-lg icon-back" @click="back"></i></span>
        <span><i class="fa fa-download"></i></span>
        <span><i class="fa fa-commenting-o"></i></span>
        <span><i class="fa fa-ellipsis-v"></i></span>
      </div>
    </modal>
    <modal v-model="modal1" class="modal-close" width="250" :closable="false">
      <div slot="header" class="modal-close-header">
        加入书架
      </div>
      <div class="modal-close-body">
        喜欢本书就加入书架吧
      </div>
      <div slot="footer" class="modal-close-footer">
        <i-button type="text" size="large" @click.native="cancel">不用了</i-button>
        <i-button type="primary" size="large" @click.native="ok">加入书架</i-button>
      </div>
    </modal>
    <modal v-model="modal4" class="modal-setting" position="bottom" width="100" :footer-hide="true" :closable="false">
      <div class="modal-setting-body" :style="{background: textOptions.background, color: textOptions.color}">
        <div class="setting-font">
          <span>A-</span>
          <slider class="setting-font-slider" v-model="sliderValue" :step="20" show-stops @on-change="changeFont"></slider>
          <span>A+</span>
        </div>
        <div class="setting-background">
          <radio-group v-model="backgroundModel" type="circle" @on-change="changeBackground" class="setting-background-group">
            <radio label="#f8f8ef" style="background:#f8f8ef"><div></div></radio>
            <radio label="#f1eabb" style="background:#f1eabb"><div></div></radio>
            <radio label="#d0fbed" style="background:#d0fbed"><div></div></radio>
            <radio label="#ece2eb" style="background:#ece2eb"><div></div></radio>
            <radio label="#3e3e3a" style="background:#3e3e3a"><div></div></radio>
          </radio-group>
        </div>
      </div>
    </modal>
  </div>
</template>
<script>
import IndexList from 'base/index-list/index-list'
import Modal from 'base/modal/modal'
import IButton from 'base/button/button'
import Radio from 'base/radio/radio'
import Slider from 'base/slider/slider'
import RadioGroup from 'base/radio/radio-group'
import apiMixin from 'common/mixins/api'
import bookMixin from 'common/mixins/book'
import {chapterDetail} from 'api/getdata'
import {mapGetters, mapMutations} from 'vuex'
import {getData, getRect, prefixStyle, getMatchedTarget} from 'common/helpers/dom'

var fromRoute = null
export default {
  mixins: [apiMixin, bookMixin],
  data() {
    return {
      chapters: [],
      backgroundModel: '#f8f8ef',
      modal1: false,
      modal2: false,
      modal3: false,
      modal4: false,
      sliderValue: 40,
      textOptions: {
        fontSize: 14,
        background: '#f8f8ef',
        color: '#000',
        lineHeight: 1,
      },
      moonMenu: {
        icon: 'moon-o',
        text: '夜间',
      }
    }
  },
  computed: {
    textStyle() {
      return [
        this.textOptions.fontSize && this.textOptions.fontSize !== 0 ? { fontSize: this.textOptions.fontSize + 'px'} : {},
        this.textOptions.background ? { background: this.textOptions.background } : {},
        this.textOptions.color ? {color: this.textOptions.color} : {},
        this.textOptions.lineHeight ? {lineHeight: this.lineHeight} : {}
      ]
    },
    iconMode() {
      return this.moonMenu.icon ? this.moonMenu.icon : null
    },
    iconText() {
      return this.moonMenu.text ? this.moonMenu.text : null
    },
    options() {
      return {
        probeType: 3,
        pullDownRefresh: true,
        pullUpLoad: true,
        mouseWheel: true
      }
    }
  },
  created() {
    this.initData()
  },
  beforeRouteEnter(to, from ,next) {
    fromRoute = from
    next()
  },
  methods: {
    async getChapterDetailById(id) {
      if (!id || id === null) {
        this.$router.back()
      }
      let c = await chapterDetail(id)
      return c
    },
    getCurrentIndex(index) {
      this.updateBook(this.findIndex(this.chapters[index].id, this.book.chapters))
    },
    initData() {
      let chapterid = this.$route.params.id
      let c = this.getChapterDetailById(chapterid)
      c.then(res => {
        let chapter = {
          id: res.chapter_detail.id,
          title: res.chapter_detail.title,
          text: res.chapter_detail.text
        }
        this.chapters.push(chapter)
      })     
    },
    showModal(e) {
      if (!this.isModalShow) {
        this.modal2 = true
        this.modal3 = true
        this.isModalShow = !this.isModalShow
      } else {
        this.modal2 = false
        this.modal3 = false
        this.modal4 = false
        this.isModalShow = !this.isModalShow
      }
    },
    back() {
      this.modal1 = true
      this.modal2 = false
      this.modal3 = false
    },
    showChapter(e) {
      this.$router.push('/book/chapter')
    },
    showSetting() {
      this.modal4 = true
      this.modal2 = false
      this.modal3 = false
      this.isModalShow = !this.isModalShow
    },
    changeMode() {
      if (!this.isMode2) {
        this.textOptions.color = '#a7a0a0'
        this.textOptions.background = '#252521'
        this.moonMenu.icon = 'sun-o'
        this.moonMenu.text = '日间'
        this.isMode2 = !this.isMode2
      } else {
        this.textOptions.color = '#000'
        this.textOptions.background = '#f8f8ef'
        this.moonMenu.icon = 'moon-o'
        this.moonMenu.text = '夜间'
        this.isMode2 = !this.isMode2
      }
    },
    changeFont(value) {
      this.textOptions.fontSize = 14 + (value - this.sliderValue) / 20 * 2
    },
    changeBackground(value) {
      this.textOptions.background = value
      if (value === '#3e3e3a') {
        this.textOptions.color = '#a7a0a0'
      } else {
        this.textOptions.color = '#000'
      }
    },
    cancel() {
      if (fromRoute.name === 'Chapter') {
        this.$router.go(-2)
      } else {
        this.$router.back()
      }
    },
    ok() {
      if (fromRoute.name === 'Chapter') {
        this.$router.go(-2)
      } else {
        this.$router.back()
      }
    },
    onPullingDown() {
      let prev = this.getPrevChapter(this.book.chapters[this.book.curChapter])
      if (!prev || prev === null) {
        this.$refs.scroll.forceUpdate()
      } else if (this.findIndex(prev.id, this.chapters) > -1) {
        this.$refs.scroll.forceUpdate()
      }else {
        let c = this.getChapterDetailById(prev.id)
        c.then(res => {
          let prevChapter = {
            id: prev.id,
            title: prev.title,
            text: res.chapter_detail.text
          }
          this.chapters.unshift(prevChapter)
          this.updateBook(this.book.prevChapter)
          this.$refs.scroll.refresh()
          this.$refs.scroll.forceUpdate()
        })
      }
    },
    onPullingUp() {
      let next = this.getNextChapter(this.book.chapters[this.book.curChapter])
      if (!next || next === null) {
        this.$refs.scroll.forceUpdate()
      } else if (this.findIndex(next.id, this.chapters) > -1) {
        this.$refs.scroll.forceUpdate()
      } else {
        let d = this.getChapterDetailById(next.id)
        d.then(res => {
          let nextChapter = {
            id: next.id,
            title: next.title,
            text: res.chapter_detail.text
          }
          this.chapters.push(nextChapter)
          this.updateBook(this.book.nextChapter)
          this.$refs.scroll.refresh()
          this.$refs.scroll.forceUpdate()
        })
      }
    }
  },
  components: {
    IndexList,
    Modal,
    IButton,
    Radio,
    Slider,
    RadioGroup
  }
}
</script>

<style lang="stylus">
  @import '~common/stylus/variable'

  .chapter-detail
    position: fixed
    left: 0
    top: 0
    z-index: 10
    width: 100%
    height: 100%
    background-color: $color-text-bg
    .chapter-detail-item
      .chapter-detail-title
        padding: 10px
      .chapter-detail-text
        line-height: 20px
        padding: 10px 10px 0 10px

    .modal-menu-top, .modal-menu-bottom
      width: 100%
      .modal-top-content, .modal-bottom-content
        display: flex
        width: 100%
        height: 40px
        align-items: center
        padding: 0 10px
        background-color: black
        & span
          color: $color-white
      .modal-top-content
        justify-content: flex-end
        & span
          flex: 1
          text-align: center
        .back
          text-align: left
          flex: 7
          .icon-back
            height: inherit
            padding: 3px 15px
      .modal-bottom-content span
        flex: 1
        display: block
        text-align: center
        font-size: $fontsize-small
    
    .modal-close
      .modal-close-header
        text-align: center
      .modal-close-body
        padding: 16px
      .modal-close-footer
        display: flex
        align-items: center
        justify-content: center

    .modal-setting
      width: 100%
      height: 80px
      .modal-setting-body
        padding: 10px 20px
        border-radius: 0
        .setting-font
          display: flex
          align-items: center
          height: 40px
          .setting-font-slider
            flex: 8
          & span
            flex: 1
            text-align: center
        .setting-background-group
          display: flex
          justify-content: space-between
</style>
