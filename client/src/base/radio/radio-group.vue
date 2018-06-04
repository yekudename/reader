<template>
    <div :class="classes" :name="name">
        <slot></slot>
    </div>
</template>
<script>
    import { oneOf, findComponentsDownward } from 'common/utils/assist';
    import Emitter from 'common/mixins/emitter';

    const prefixCls = 'radio-group';

    let seed = 0;
    const now = Date.now();
    const getUuid = () => `RadioGroup_${now}_${seed++}`;

    export default {
        name: 'RadioGroup',
        mixins: [ Emitter ],
        props: {
            value: {
                type: [String, Number],
                default: ''
            },
            size: {
                validator (value) {
                    return oneOf(value, ['small', 'large', 'default']);
                }
            },
            type: {
                validator (value) {
                    return oneOf(value, ['button', 'circle']);
                }
            },
            vertical: {
                type: Boolean,
                default: false
            },
            name: {
                type: String,
                default: getUuid
            }
        },
        data () {
            return {
                currentValue: this.value,
                childrens: []
            };
        },
        computed: {
            classes () {
                return [
                    `${prefixCls}`,
                    {
                        [`${prefixCls}-${this.size}`]: !!this.size,
                        [`radio-${this.size}`]: !!this.size,
                        [`${prefixCls}-${this.type}`]: !!this.type,
                        [`${prefixCls}-vertical`]: this.vertical
                    }
                ];
            }
        },
        mounted () {
            this.updateValue();
        },
        methods: {
            updateValue () {
                this.childrens = findComponentsDownward(this, 'Radio');
                if (this.childrens) {
                    this.childrens.forEach(child => {
                        child.currentValue = this.value === child.label;
                        child.group = true;
                    });
                }
            },
            change (data) {
                this.currentValue = data.value;
                this.updateValue();
                this.$emit('input', data.value);
                this.$emit('on-change', data.value);
                this.dispatch('FormItem', 'on-form-change', data.value);
            }
        },
        watch: {
            value () {
                this.currentValue = this.value;
                this.updateValue();
            }
        }
    };
</script>

<style lang="stylus">
  @import '~common/stylus/variable'

  .radio-group
    display: inline-block
    font-size: $font-size-small
    vertical-align: middle
    .radio-group-vertical
      .radio-wrapper
        display: block
        height: 30px
        line-height: 30px

  .radio-group-circle
    font-size: 0
    -webkit-text-size-adjust: none

    .radio
      width: 0
      margin-right: 0

    .radio-wrapper
      display: inline-block
      box-sizing: border-box
      width: 30px
      height: 30px
      line-height: 30px
      margin: 0
      font-size: $font-size-small
      color: $btn-default-color
      transition: all $transition-time ease-in-out
      cursor: pointer
      background: yellow
      position: relative
      border-radius: 50%

      > span
        margin-left: 0

      .radio-inner,input
        opacity: 0
        width: 0
        height: 0

    .radio-wrapper-checked
      background: #fff
      border: 2px solid $primary-color
      color: $primary-color
      z-index: 1

  .radio-group-button
    font-size: 0
    --webkit-text-size-adjust: none

    .radio
      width: 0
      margin-right: 0

    .radio-wrapper
      display: inline-block
      height: $btn-circle-size
      line-height: $btn-circle-size - 2px
      margin: 0
      padding: 0 16px - 1px
      font-size: $font-size-small
      color: $btn-default-color
      transition: all $transition-time ease-in-out
      cursor: pointer
      border: 1px solid $border-color-base
      border-left: 0
      background: #ffffff
      position: relative

      > span
        margin-left: 0

      &:before, &:after
        content: ''
        display: block
        position: absolute
        width: 1px
        height: 100%
        left: -1px
        top: 0
        background: $border-color-base
        transition: all $transition-time ease-in-out

      &:after
        height: $btn-circle-size + 4px
        left: -1px
        top: -3px
        background: fade($primary-color, 20%)
        opacity: 0

      &:first-child
        border-radius: $btn-border-radius 0 0 $btn-border-radius
        border-left: 1px solid $border-color-base
        &:before, &:after
          display: none

      &:last-child
        border-radius: 0 $btn-border-radius $btn-border-radius 0

      &:first-child:last-child
        border-radius: $btn-border-radius

      &:hover
        position: relative
        color: $primary-color
        & .radio
          background-color: black

      .radio-inner,input
        opacity: 0
        width: 0
        height: 0

      
      .radio-checked
        background: #fff
        border-color: $primary-color
        color: $primary-color
        box-shadow: -1px 0 0 0 $primary-color
        z-index: 1

        &:before
          background: $primary-color
          opacity: 0.1

        &.radio-focus
          box-shadow: -1px 0 0 0 $primary-color, 0 0 0 2px fade($primary-color, 20%)
          transition: all $transition-time ease-in-out
          &:after
            left: -3px
            top: -3px
            opacity: 1
            background: fade($primary-color, 20%)
          &:first-child
            box-shadow: 0 0 0 2px fade($primary, 20%)
        
        &:first-child
          border-color: $primary-color
          box-shadow: none

        &:hover
          border-color: tint($primary-color, 20%)
          color: tint($primary-color, 20%)

        &:active
          border-color: shade($primary-color, 5%)
          color: shade($primary-color, 5%)

      .radio-disabled
        border-color: $border-color-base
        background-color: $background-color-base
        cursor: $cursor-disabled
        color: #ccc

        &:first-child,
        &:hover
          border-color: $border-color-base
          background-color: $background-color-base
          color: #ccc
        &:first-child
          border-left-color: $border-color-base

      .radio-disabled.radio-wrapper-checked
        color: #fff
        background-color: #e6e6e6
        border-color: $border-color-base
        box-shadow: none!important
</style>

