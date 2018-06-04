<template>
    <button
        :type="htmlType"
        :class="classes"
        :disabled="disabled"
        @click="handleClick">
        <Icon class="ivu-load-loop" type="load-c" v-if="loading"></Icon>
        <Icon :type="icon" v-if="icon && !loading"></Icon>
        <span v-if="showSlot" ref="slot"><slot></slot></span>
    </button>
</template>
<script>
    import Icon from '../icon/icon'
    import { oneOf } from 'common/utils/assist'

    const prefixCls = 'btn';

    export default {
        name: 'Button',
        components: { Icon },
        props: {
            type: {
                validator (value) {
                    return oneOf(value, ['primary', 'ghost', 'dashed', 'text', 'info', 'success', 'warning', 'error', 'default'])
                }
            },
            shape: {
                validator (value) {
                    return oneOf(value, ['circle', 'circle-outline'])
                }
            },
            size: {
                validator (value) {
                    return oneOf(value, ['small', 'large', 'default'])
                }
            },
            loading: Boolean,
            disabled: Boolean,
            htmlType: {
                default: 'button',
                validator (value) {
                    return oneOf(value, ['button', 'submit', 'reset'])
                }
            },
            icon: String,
            long: {
                type: Boolean,
                default: false
            }
        },
        data () {
            return {
                showSlot: true
            };
        },
        computed: {
            classes () {
                return [
                    `${prefixCls}`,
                    {
                        [`${prefixCls}-${this.type}`]: !!this.type,
                        [`${prefixCls}-long`]: this.long,
                        [`${prefixCls}-${this.shape}`]: !!this.shape,
                        [`${prefixCls}-${this.size}`]: !!this.size,
                        [`${prefixCls}-loading`]: this.loading != null && this.loading,
                        [`${prefixCls}-icon-only`]: !this.showSlot && (!!this.icon || this.loading)
                    }
                ];
            }
        },
        methods: {
            handleClick (event) {
                this.$emit('click', event);
            }
        },
        mounted () {
            this.showSlot = this.$slots.default !== undefined;
        }
    };
</script>

<style lang="stylus">
  @import '~common/stylus/variable'
  @import '~common/stylus/button'

  .btn
    btn()
    btn-default()

  .btn-long
    width: 100%

  .btn > .icon + span, .btn > span + .icon
    margin-left: 4px

  .btn-primary
    button-variant($btn-primary-color, $btn-primary-bg, $primary-color)

  .btn-default
    button-variant($btn-default-color, $btn-default-bg, $btn-default-border)

  .btn-ghost
    button-variant($btn-ghost-color, $btn-ghost-bg, $btn-ghost-border)


  .btn-dashed
    button-variant($btn-ghost-color, $btn-ghost-bg, $btn-ghost-border)


  .btn-text
    button-variant($btn-ghost-color, $btn-ghost-bg, transparent)


  .btn-success
    button-variant($btn-primary-color, $success-color, $success-color)


  .btn-warning 
    button-color($btn-primary-color, $warning-color, $warning-color)


  .btn-error 
    button-color($btn-primary-color, $error-color, $error-color)


  .btn-info 
    button-color($btn-primary-color, $info-color, $info-color)

  .btn-large
    button-size($btn-padding-large, $btn-font-size-large, $btn-border-radius)

  .btn-small
    button-size($btn-padding-small, $btn-font-size, $btn-border-radius-small)


  .btn-circle,
  .btn-circle-outline 
    btn-circle(btn)
    
    &:before 
      position: absolute
      top: -1px
      left: -1px
      bottom: -1px
      right: -1px
      background: #fff
      opacity: 0.35
      content: ''
      border-radius: inherit
      z-index: 1
      transition: opacity @transition-time
      pointer-events: none
      display: none
    
    &&-loading 
      pointer-events: none
      position: relative

      &:before
        display: block
</style>