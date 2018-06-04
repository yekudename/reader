<template>
  <transition name="slide">
    <div class="singer-detail">
      <c-button :primary="options.primary" :light="options.light" @click="showPopup">
        <div>按钮</div>
      </c-button>
      <popup ref="popup"></popup>
    </div>
  </transition>
</template>

<script>
import {mapGetters} from 'vuex'
import CButton from 'base/button/button'
import Popup from 'base/popup/popup'

export default {
  name: 'singer-detail',
  computed: {
    options() {
      return {
        primary: true,
        light: true
      }
    },
    ...mapGetters([
      'singer'
    ])
  },
  created() {
    console.log(this.singer)
  },
  methods: {
    showPopup() {
      console.log('button-clicked')
      this.$refs.popup.show()
    }
  },
  components: {
    CButton,
    Popup
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @require '~common/stylus/variable'
  .singer-detail
    position: fixed
    z-index: 100
    top: 0
    bottom: 0
    left: 0
    right: 0
    background: $color-background
  .slide-enter-active,.slide-leave-active
    transition: all 0.5s
  .slide-enter,.slide-leave-to
    transform: translate3d(100%, 0, 0)
</style>
