<template>
    <div v-transfer-dom :data-transfer="transfer" class="modal-root">
        <transition :name="transitionNames[1]">
            <div :class="maskClasses" v-show="visible" @click="mask"></div>
        </transition>
        <div :class="wrapClasses" @click="handleWrapClick">
            <transition :name="transitionNames[0]" @after-leave="animationFinish">
                <div :class="classes" :style="mainStyles" v-show="visible">
                    <div :class="[prefixCls + '-content']">
                        <a :class="[prefixCls + '-close']" v-if="closable" @click="close">
                            <slot name="close">
                                <i class="fa fa-close"></i>
                            </slot>
                        </a>
                        <div :class="[prefixCls + '-header']" v-if="showHead"><slot name="header"><div :class="[prefixCls + '-header-inner']">{{ title }}</div></slot></div>
                        <div :class="[prefixCls + '-body']"><slot></slot></div>
                        <div :class="[prefixCls + '-footer']" v-if="!footerHide">
                            <slot name="footer">
                                <i-button type="error" size="small" @click.native="cancel">{{ localeCancelText }}</i-button>
                                <i-button type="primary" size="small" :loading="buttonLoading" @click.native="ok">{{ localeOkText }}</i-button>
                            </slot>
                        </div>
                    </div>
                </div>
            </transition>
        </div>
    </div>
</template>
<script>
    import iButton from '../button/button.vue';
    import TransferDom from '../../directives/transfer-dom';
    import Emitter from 'common/mixins/emitter';

    const prefixCls = 'modal';

    export default {
        name: 'Modal',
        mixins: [Emitter],
        components: {iButton },
        directives: { TransferDom },
        props: {
            value: {
                type: Boolean,
                default: false
            },
            closable: {
                type: Boolean,
                default: true
            },
            maskClosable: {
                type: Boolean,
                default: true
            },
            maskHidden: {
                type: Boolean,
                default: false
            },
            position: {
                type: String,
                default: ''
            },
            title: {
                type: String
            },
            width: {
                type: [Number, String],
                default: 520
            },
            okText: {
                type: String
            },
            cancelText: {
                type: String
            },
            loading: {
                type: Boolean,
                default: false
            },
            styles: {
                type: Object
            },
            className: {
                type: String
            },
            // for instance
            footerHide: {
                type: Boolean,
                default: false
            },
            scrollable: {
                type: Boolean,
                default: false
            },
            transitionNames: {
                type: Array,
                default () {
                    return ['ease', 'fade'];
                }
            },
            transfer: {
                type: Boolean,
                default: false
            }
        },
        data () {
            return {
                prefixCls: prefixCls,
                wrapShow: false,
                showHead: true,
                buttonLoading: false,
                visible: this.value
            };
        },
        computed: {
            wrapClasses () {
                return [
                    `${prefixCls}-wrap`,
                    {
                        [`${prefixCls}-hidden`]: !this.wrapShow,
                        [`${this.className}`]: !!this.className,
                        ['modal-' + `${this.position}`]: !!this.position
                    }
                ];
            },
            maskClasses () {
                return [
                    `${prefixCls}-mask`,
                    {
                        [`${prefixCls}-mask-hidden`]: this.maskHidden
                    }
                ]
            },
            classes () {
                return `${prefixCls}`;
            },
            mainStyles () {
                let style = {};

                const width = parseInt(this.width);
                const styleWidth = {
                    width: width <= 100 ? `${width}%` : `${width}px`
                };

                const customStyle = this.styles ? this.styles : {};

                Object.assign(style, styleWidth, customStyle);

                return style;
            },
            localeOkText () {
                if (this.okText === undefined) {
                    return 'ok'
                } else {
                    return this.okText;
                }
            },
            localeCancelText () {
                if (this.cancelText === undefined) {
                    return 'cancel'
                } else {
                    return this.cancelText;
                }
            }
        },
        methods: {
            close () {
                this.visible = false;
                this.$emit('input', false);
                this.$emit('on-cancel');
            },
            mask () {
                if (this.maskClosable) {
                    this.close();
                }
            },
            handleWrapClick (event) {
                // use indexOf,do not use === ,because ivu-modal-wrap can have other custom className
                const className = event.target.getAttribute('class');
                if (className && className.indexOf(`${prefixCls}-wrap`) > -1) this.mask();
            },
            cancel () {
                this.close();
            },
            ok () {
                if (this.loading) {
                    this.buttonLoading = true;
                } else {
                    this.visible = false;
                    this.$emit('input', false);
                }
                this.$emit('on-ok');
            },
            EscClose (e) {
                if (this.visible && this.closable) {
                    if (e.keyCode === 27) {
                        this.close();
                    }
                }
            },
            animationFinish() {
                this.$emit('on-hidden');
            }
        },
        mounted () {
            if (this.visible) {
                this.wrapShow = true;
            }

            let showHead = true;

            if (this.$slots.header === undefined && !this.title) {
                showHead = false;
            }

            this.showHead = showHead;

            // ESC close
            document.addEventListener('keydown', this.EscClose);
        },
        beforeDestroy () {
            document.removeEventListener('keydown', this.EscClose);
            // this.removeScrollEffect();
        },
        watch: {
            value (val) {
                this.visible = val;
            },
            visible (val) {
                if (val === false) {
                    this.buttonLoading = false;
                    this.timer = setTimeout(() => {
                        this.wrapShow = false;
                        // this.removeScrollEffect();
                    }, 300);
                } else {
                    if (this.timer) clearTimeout(this.timer);
                    this.wrapShow = true;
                    // if (!this.scrollable) {
                    //     this.addScrollEffect();
                    // }
                }
                this.broadcast('Table', 'on-visible-change', val);
                this.broadcast('Slider', 'on-visible-change', val);  // #2852
                this.$emit('on-visible-change', val);
            },
            loading (val) {
                if (!val) {
                    this.buttonLoading = false;
                }
            },
            // scrollable (val) {
            //     if (!val) {
            //         this.addScrollEffect();
            //     } else {
            //         this.removeScrollEffect();
            //     }
            // },
            title (val) {
                if (this.$slots.header === undefined) {
                    this.showHead = !!val;
                }
            }
        }
    };
</script>

<style lang="stylus">
  @import '~common/stylus/variable'
  .modal-root
    width: auto
    margin: 0 auto
    position: relative
    outline: none

    .modal-hidden
      display: none !important

    .modal-wrap
      position: fixed
      overflow: auto
      top: 50%
      left: 50%
      width: inherit
      z-index: $zIndex-modal
      outline: 0
      transform: translate3d(-50%, -50%, 0)

    .modal-wrap *
      box-sizing: border-box
      -webkit-tap-highlight-color: rgba(0, 0, 0, 0)
    
    .modal-top
      top: 0
      right: auto
      bottom: auto
      left: 50%
      transform: translate3d(-50%, 0, 0)
    .modal-right
      right: 0
      top: 50%
      bottom: auto
      left: auto
      transform: translate3d(0, -50%, 0)
    .modal-bottom
      top: auto
      right: auto
      left: 50%
      bottom: 0
      transform: translate3d(-50%, 0, 0)
    .modal-left
      left: 0
      top: 50%
      bottom: auto
      right: auto
      transform: translate3d(-50%, 0, 0)

    .modal-mask
      position: fixed
      top: 0
      bottom: 0
      left: 0
      right: 0
      background-color: rgba(55, 55, 55, 0.6)
      height: 100%
      z-index: $zIndex-modal
    .modal-mask-hidden
      display: none

    .modal-content
      position: relative
      background-color: $color-white
      border: 0
      border-radius: 2px
      background-clip: padding-box

      .modal-close
        font-size: $font-size-small
        position: absolute
        right: 16px
        top: 8px
        overflow: hidden
        cursor: pointer

        .modal-close-empty
          font-size: 22px
          color: $color-text
          transition: color .2s ease;
          position: relative
          top: 0
          &:hover
            color: #444

      .modal-header
        border-bottom: 1px solid $color-row-line
        padding: 14px 16px
        line-height: 1
        p,.modal-inner
            display: inline-block
            width: 100%
            height: 20px
            line-height: 20px
            font-size: $fontsize-medium
            color: $color-title
            font-weight: bold
            overflow: hidden
            text-overflow: ellipsis
            white-space: nowrap

      .modal-body
        font-size: $fontsize-small
        line-height: 1.5

      .modal-footer
        border-top: 1px solid $color-row-line
        padding: 12px 18px 12px 18px
        text-align: right
        button + button
          margin-left: 8px
          margin-bottom: 0
</style>
