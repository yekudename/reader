<template>
  <label :class="wrapClasses">
    <span :class="radioClasses">
      <span :class="innerClasses"></span>
      <input
          type="radio"
          :class="inputClasses"
          :disabled="disabled"
          :checked="currentValue"
          :name="groupName"
          @change="change"
          @focus="onFocus"
          @blur="onBlur">
    </span>
    <slot>{{ label }}</slot>
  </label>
</template>
<script>
import { findComponentUpward, oneOf } from "common/utils/assist";
import Emitter from "common/mixins/emitter";

const prefixCls = "radio";

export default {
  name: "Radio",
  mixins: [Emitter],
  props: {
    value: {
      type: [String, Number, Boolean],
      default: false
    },
    trueValue: {
      type: [String, Number, Boolean],
      default: true
    },
    falseValue: {
      type: [String, Number, Boolean],
      default: false
    },
    label: {
      type: [String, Number]
    },
    disabled: {
      type: Boolean,
      default: false
    },
    size: {
      validator(value) {
        return oneOf(value, ["small", "large", "default"]);
      }
    },
    name: {
      type: String
    }
  },
  data() {
    return {
      currentValue: this.value,
      group: false,
      groupName: this.name,
      parent: findComponentUpward(this, "RadioGroup"),
      focusWrapper: false,
      focusInner: false
    };
  },
  computed: {
    wrapClasses() {
      return [
        `${prefixCls}-wrapper`,
        {
          [`${prefixCls}-group-item`]: this.group,
          [`${prefixCls}-wrapper-checked`]: this.currentValue,
          [`${prefixCls}-wrapper-disabled`]: this.disabled,
          [`${prefixCls}-${this.size}`]: !!this.size,
          [`${prefixCls}-focus`]: this.focusWrapper
        }
      ];
    },
    radioClasses() {
      return [
        `${prefixCls}`,
        {
          [`${prefixCls}-checked`]: this.currentValue,
          [`${prefixCls}-disabled`]: this.disabled
        }
      ];
    },
    innerClasses() {
      return [
        `${prefixCls}-inner`,
        {
          [`${prefixCls}-focus`]: this.focusInner
        }
      ];
    },
    inputClasses() {
      return `${prefixCls}-input`;
    }
  },
  mounted() {
    if (this.parent) {
      this.group = true;
      if (this.name && this.name !== this.parent.name) {
        /* eslint-disable no-console */
        if (console.warn) {
          console.warn("[iview] Name does not match Radio Group name.");
        }
        /* eslint-enable no-console */
      } else {
        this.groupName = this.parent.name;
      }
    }

    if (this.group) {
      this.parent.updateValue();
    } else {
      this.updateValue();
    }
  },
  methods: {
    change(event) {
      if (this.disabled) {
        return false;
      }

      const checked = event.target.checked;
      this.currentValue = checked;

      const value = checked ? this.trueValue : this.falseValue;
      this.$emit("input", value);

      if (this.group) {
        if (this.label !== undefined) {
          this.parent.change({
            value: this.label,
            checked: this.value
          });
        }
      } else {
        this.$emit("on-change", value);
        this.dispatch("FormItem", "on-form-change", value);
      }
    },
    updateValue() {
      this.currentValue = this.value === this.trueValue;
    },
    onBlur() {
      this.focusWrapper = false;
      this.focusInner = false;
    },
    onFocus() {
      if (this.group && this.parent.type === "button") {
        this.focusWrapper = true;
      } else {
        this.focusInner = true;
      }
    }
  },
  watch: {
    value(val) {
      if (val === this.trueValue || val === this.falseValue) {
        this.updateValue();
      } else {
        throw "Value should be trueValue or falseValue.";
      }
    }
  }
};
</script>

<style lang="stylus">
@import '~common/stylus/variable'

.radio-wrapper
  font-size: $font-size-small
  vertical-align: middle
  display: inline-block
  position: relative
  white-space: nowrap
  margin-right: 8px
  cursor: pointer

  .radio-disabled
    cursor: $cursor-disabled

.radio-large
  font-size: $font-size-base
  & .radio-inner
    width: 16px
    height: 16px
    &:after
      width: 10px
      height: 10px
  &.radio-wrapper, & .radio-wrapper
    font-size: $font-size-base

.radio-small
  & .raido-inner
    width: 12px
    height: 12px
    &:after
      width: 6px
      height: 6px

  .radio-checked
    .radio-inner
      border-color: $primary-color
      &:after
        opacity: 1
        transform: scale(1)
        transition: all $transition-time $ease-in-out
    &:hover
      .radio-inner
        border-color: $primary-color

  .radio-disabled
    cursor: $cursor-disabled
    .radio-input
      cursor: $cursor-disabled

    &:hover
      .radio-inner
        border-color: $border-color-base
    .radio-inner
      border-color: $border-color-base
      background-color: #f3f3f3
      &:after
        background-color: #cccccc
    .radio-disabled + span
      color: #ccc

  .radio
    display: inline-block;
    margin-right: 4px;
    white-space: nowrap;
    position: relative;
    line-height: 1;
    vertical-align: middle;
    cursor: pointer;

    &:hover
      .radio-inner
        border-color: #bcbcbc;

    .radio-inner
      display: inline-block;
      width: 14px;
      height: 14px;
      position: relative;
      top: 0;
      left: 0;
      background-color: #ffffff;
      border: 1px solid $border-color-base;
      border-radius: 50%;
      transition: all $transition-time $ease-in-out;

      &:after
        position: absolute;
        width: 8px;
        height: 8px;
        left: 2px;
        top: 2px;
        border-radius: $border-radius-base;
        display: table;
        border-top: 0;
        border-left: 0;
        content: ' ';
        background-color: $primary-color;
        opacity: 0;
        transition: all $transition-time $ease-in-out;
        transform: scale(0);

    .radio-input
      position: absolute
      top: 0
      bottom: 0
      left: 0
      right: 0
      z-index: 1
      opacity: 0
      cursor: pointer
</style>

