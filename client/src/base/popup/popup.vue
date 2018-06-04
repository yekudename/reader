<template>
  <transition :name="currentTransition">
    <div class="popup" :style="{'z-index':zIndex}" :class="rootClass" v-show="isVisible">
      <div class="popup-mask" @click="maskClick">
        <slot name="mask"></slot>
      </div>
      <div class="popup-container" :class="{'popup-center':center}">
        <slot></slot>
      </div>
    </div>
  </transition>
</template>

<script>
import apiMixin from 'common/mixins/api'
const EVENT_MASK_CLICK = 'mask-click'

export default {
  name: 'popup',
  mixins: [apiMixin],
  props: {
    position: {
      type: String,
      default: ''
    },
    mask: {
      type: Boolean,
      default: false
    },
    content: {
      type: String,
      default: ''
    },
    center: {
      type: Boolean,
      default: true
    },
    zIndex: {
      type: Number,
      default: 100
    },
    popupTransition: {
      type: String,
      default: 'popup-slide'
    }
  },
  data() {
    return {
      currentTransition: this.popupTransition
    }
  },
  computed: {
    rootClass() {
      const cls = {
        'popup_mask': this.mask
      }
      if (this.type) {
        cls[`${this.type}`] = true
      }
      if (this.position) {
        cls['popup-' + `${this.position}`] = true
      }
      return cls
    }
  },
  methods: {
    maskClick(e) {
      this.$emit(EVENT_MASK_CLICK, e)
    }
  },
  beforeMount() {
    if (this.popupTransition !== 'popup-fade') {
      this.currentTransition = `popup-slide-${ this.position }`;
    }
  },
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "~common/stylus/variable"
  .popup
    position: fixed
    background: $color-dark
    left: 50%
    top: 50%
    transform: translate3d(-50%, -50%, 0)
    transition: .2s ease-out
    pointer-events: none
  .popup-top
    top: 0
    right: auto
    bottom: auto
    left: 50%
    transform: translate3d(-50%, 0, 0)
  .popup-right
    right: 0
    top: 50%
    bottom: auto
    left: auto
    transform: translate3d(0, -50%, 0)
  .popup-bottom
    top: auto
    right: auto
    left: 50%
    bottom: 0
    transform: translate3d(-50%, 0, 0)
  .popup-left
    left: 0
    top: 50%
    bottom: auto
    right: auto
    transform: translate3d(-50%, 0, 0)
    .popup-container
      position: absolute
      width: 100
      height: 100%
  // .popup_mask
  //   pointer-events: auto
  //   .popup-mask
  //     display: block
  // .popup-mask, .popup-container
  //   position: absolute
  //   left: 0
  //   top: 0
  //   width: 100%
  //   height: 100%
  // .popup-mask
  //   display: none
  //   overflow: hidden
  //   background-color: $popup-mask-bgc
  //   opacity: $popup-mask-opacity
  //   pointer-events auto
  //   &::before
  //     content: "."
  //     display: block
  //     width: 1px
  //     height: 1px
  //     background-color: rgba(0, 0, 0, .1)
  //     margin-left: -10px

  .popup-slide-top-enter,
  .popup-slide-top-leave-active
    transform: translate3d(-50%, -100%, 0)

  .popup-slide-right-enter,
  .popup-slide-right-leave-active
    transform: translate3d(100%, -50%, 0)

  .popup-slide-bottom-enter,
  .popup-slide-bottom-leave-active
    transform: translate3d(-50%, 100%, 0)

  .popup-slide-left-enter,
  .popup-slide-leave-active
    transform: translate3d(-100%, -50%, 0)

  .popup-fade-enter,
  .popup-fade-leave-active
    opacity: 0
</style>
