<template>
  <div :class="[prefixCls]" @mouseenter="handleShowPopper" @mouseleave="handleClosePopper">
    <div :class="[prefixCls + '-rel']" ref="reference">
      <slot></slot>
    </div>
    <transition name="fade">
      <div
        :class="[prefixCls + '-popper']"
        ref="popper"
        v-show="!disabled && (visible || always)"
        @mouseenter="handleShowPopper"
        @mouseleave="handleClosePopper"
        :data-transfer="transfer"
        v-transfer-dom>
        <div :class="[prefixCls + '-content']">
          <div :class="[prefixCls + '-arrow']"></div>
          <div :class="[prefixCls + '-inner']"><slot name="content">{{ content }}</slot></div>
        </div>
      </div>
    </transition>
  </div>
</template>
<script>
import Popper from '../base/popper'
import TransferDom from '../../directives/transfer-dom'
import { oneOf } from 'common/utils/assist'

const prefixCls = 'tooltip'

export default {
  name: 'Tooltip',
  directives: { TransferDom },
  mixins: [Popper],
  props: {
    placement: {
      validator (value) {
        return oneOf(value, ['top', 'top-start', 'top-end', 'bottom', 'bottom-start', 'bottom-end', 'left', 'left-start', 'left-end', 'right', 'right-start', 'right-end']);
      },
      default: 'bottom'
    },
    content: {
      type: [String, Number],
        default: ''
    },
    delay: {
      type: Number,
      default: 100
    },
    disabled: {
      type: Boolean,
      default: false
    },
    controlled: {    // under this prop,Tooltip will not close when mouseleave
      type: Boolean,
      default: false
    },
    always: {
      type: Boolean,
      default: false
    },
    transfer: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
    prefixCls: prefixCls
    }
  },
  watch: {
    content () {
      this.updatePopper()
    }
  },
  methods: {
    handleShowPopper() {
      if (this.timeout) clearTimeout(this.timeout)
        this.timeout = setTimeout(() => {
          this.visible = true
        }, this.delay)
    },
    handleClosePopper() {
      if (this.timeout) {
        clearTimeout(this.timeout)
        if (!this.controlled) {
          this.timeout = setTimeout(() => {
            this.visible = false
          }, 100)
        }
      }
    }
  },
  mounted () {
    if (this.always) {
      this.updatePopper()
    }
  }
}
</script>

<style lang="stylus">
  @import '~common/stylus/variable'
  @import '~common/stylus/mixin'

  $tooltip-max-width = 250px
  $tooltip-arrow-width = 5px
  $tooltip-distance = $tooltip-arrow-width - 1 + 4

  .tooltip
    display: inline-block

    .tooltip-rel
      display: inline-block
      position: relative

    .tooltip-popper
      display: block
      visibility: visible
      font-size: $fontsize-small
      line-height: $line-height-base
      position: absolute
      z-index: $zindex-tooltip

    .tooltip-inner
        max-width: $tooltip-max-width
        min-height: 34px
        padding: 8px 12px
        color: @tooltip-color
        text-align: left
        text-decoration: none
        background-color: @tooltip-bg
        border-radius: @border-radius-small
        box-shadow: @shadow-base
        white-space: nowrap

    .tooltip-arrow
        position: absolute
        width: 0
        height: 0
        border-color: transparent
        border-style: solid
        
    
</style>
