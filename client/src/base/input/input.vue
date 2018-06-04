<template>
  <div :class="wrapClasses">
    <template v-if="type !== 'textarea'">
      <div :class="[prefixCls + '-group-prepend']" v-if="prepend" v-show="slotReady"><slot name="prepend"></slot></div>
      <i class="icon" :class="['fa fa-close', prefixCls + '-icon', prefixCls + '-icon-clear' , prefixCls + '-icon-normal']" v-if="clearable && currentValue" @click="handleClear"></i>
      <i class="icon" :class="['fa fa-' + icon, prefixCls + '-icon', prefixCls + '-icon-normal']" v-else-if="icon" @click="handleIconClick"></i>
      <transition name="fade">
        <i class="icon ivu-icon-load-c ivu-load-loop" :class="[prefixCls + '-icon', prefixCls + '-icon-validate']" v-if="!icon"></i>
      </transition>
      <input
        :id="elementId"
        :autocomplete="autocomplete"
        :spellcheck="spellcheck"
        ref="input"
        :type="type"
        :class="inputClasses"
        :placeholder="placeholder"
        :disabled="disabled"
        :maxlength="maxlength"
        :readonly="readonly"
        :name="name"
        :value="currentValue"
        :number="number"
        :autofocus="autofocus"
        @keyup.enter="handleEnter"
        @keyup="handleKeyup"
        @keypress="handleKeypress"
        @keydown="handleKeydown"
        @focus="handleFocus"
        @blur="handleBlur"
        @input="handleInput"
        @change="handleChange">
      <div :class="[prefixCls + '-group-append']" v-if="append" v-show="slotReady"><slot name="append"></slot></div>
    </template>
    <textarea
      v-else
      :id="elementId"
      :wrap="wrap"
      :autocomplete="autocomplete"
      :spellcheck="spellcheck"
      ref="textarea"
      :class="textareaClasses"
      :style="textareaStyles"
      :placeholder="placeholder"
      :disabled="disabled"
      :rows="rows"
      :maxlength="maxlength"
      :readonly="readonly"
      :name="name"
      :value="currentValue"
      :autofocus="autofocus"
      @keyup.enter="handleEnter"
      @keyup="handleKeyup"
      @keypress="handleKeypress"
      @keydown="handleKeydown"
      @focus="handleFocus"
      @blur="handleBlur"
      @input="handleInput">
    </textarea>
  </div>
</template>
<script>
import { oneOf, findComponentUpward } from "common/utils/assist";
import calcTextareaHeight from "common/utils/calcTextareaHeight";
import Emitter from "common/mixins/emitter";

const prefixCls = "input";

export default {
  name: "Input",
  mixins: [Emitter],
  props: {
    type: {
      validator(value) {
        return oneOf(value, [
          "text",
          "textarea",
          "password",
          "url",
          "email",
          "date"
        ]);
      },
      default: "text"
    },
    value: {
      type: [String, Number],
      default: ""
    },
    size: {
      validator(value) {
        return oneOf(value, ["small", "large", "default"]);
      }
    },
    placeholder: {
      type: String,
      default: ""
    },
    maxlength: {
      type: Number
    },
    disabled: {
      type: Boolean,
      default: false
    },
    icon: String,
    autosize: {
      type: [Boolean, Object],
      default: false
    },
    rows: {
      type: Number,
      default: 2
    },
    readonly: {
      type: Boolean,
      default: false
    },
    name: {
      type: String
    },
    number: {
      type: Boolean,
      default: false
    },
    autofocus: {
      type: Boolean,
      default: false
    },
    spellcheck: {
      type: Boolean,
      default: false
    },
    autocomplete: {
      validator(value) {
        return oneOf(value, ["on", "off"]);
      },
      default: "off"
    },
    clearable: {
      type: Boolean,
      default: false
    },
    elementId: {
      type: String
    },
    wrap: {
      validator(value) {
        return oneOf(value, ["hard", "soft"]);
      },
      default: "soft"
    }
  },
  data() {
    return {
      currentValue: this.value,
      prefixCls: prefixCls,
      prepend: true,
      append: true,
      slotReady: false,
      textareaStyles: {}
    };
  },
  computed: {
    wrapClasses() {
      return [
        `${prefixCls}-wrapper`,
        {
          [`${prefixCls}-wrapper-${this.size}`]: !!this.size,
          [`${prefixCls}-type`]: this.type,
          [`${prefixCls}-group`]: this.prepend || this.append,
          [`${prefixCls}-group-${this.size}`]:
            (this.prepend || this.append) && !!this.size,
          [`${prefixCls}-group-with-prepend`]: this.prepend,
          [`${prefixCls}-group-with-append`]: this.append,
          [`${prefixCls}-hide-icon`]: this.append // #554
        }
      ];
    },
    inputClasses() {
      return [
        `${prefixCls}`,
        {
          [`${prefixCls}-${this.size}`]: !!this.size,
          [`${prefixCls}-disabled`]: this.disabled
        }
      ];
    },
    textareaClasses() {
      return [
        `${prefixCls}`,
        {
          [`${prefixCls}-disabled`]: this.disabled
        }
      ];
    }
  },
  methods: {
    handleEnter(event) {
      this.$emit("on-enter", event);
    },
    handleKeydown(event) {
      this.$emit("on-keydown", event);
    },
    handleKeypress(event) {
      this.$emit("on-keypress", event);
    },
    handleKeyup(event) {
      this.$emit("on-keyup", event);
    },
    handleIconClick(event) {
      this.$emit("on-click", event);
    },
    handleFocus(event) {
      this.$emit("on-focus", event);
    },
    handleBlur(event) {
      this.$emit("on-blur", event);
      if (
        !findComponentUpward(this, [
          "DatePicker",
          "TimePicker",
          "Cascader",
          "Search"
        ])
      ) {
        this.dispatch("FormItem", "on-form-blur", this.currentValue);
      }
    },
    handleInput(event) {
      let value = event.target.value;
      if (this.number)
        value = Number.isNaN(Number(value)) ? value : Number(value);
      this.$emit("input", value);
      this.setCurrentValue(value);
      this.$emit("on-change", event);
    },
    handleChange(event) {
      this.$emit("on-input-change", event);
    },
    setCurrentValue(value) {
      if (value === this.currentValue) return;
      this.$nextTick(() => {
        this.resizeTextarea();
      });
      this.currentValue = value;
      if (
        !findComponentUpward(this, [
          "DatePicker",
          "TimePicker",
          "Cascader",
          "Search"
        ])
      ) {
        this.dispatch("FormItem", "on-form-change", value);
      }
    },
    resizeTextarea() {
      const autosize = this.autosize;
      if (!autosize || this.type !== "textarea") {
        return false;
      }

      const minRows = autosize.minRows;
      const maxRows = autosize.maxRows;

      this.textareaStyles = calcTextareaHeight(
        this.$refs.textarea,
        minRows,
        maxRows
      );
    },
    focus() {
      if (this.type === "textarea") {
        this.$refs.textarea.focus();
      } else {
        this.$refs.input.focus();
      }
    },
    blur() {
      if (this.type === "textarea") {
        this.$refs.textarea.blur();
      } else {
        this.$refs.input.blur();
      }
    },
    handleClear() {
      const e = { target: { value: "" } };
      this.$emit("input", "");
      this.setCurrentValue("");
      this.$emit("on-change", e);
    }
  },
  watch: {
    value(val) {
      this.setCurrentValue(val);
    }
  },
  mounted() {
    if (this.type !== "textarea") {
      this.prepend = this.$slots.prepend !== undefined;
      this.append = this.$slots.append !== undefined;
    } else {
      this.prepend = false;
      this.append = false;
    }
    this.slotReady = true;
    this.resizeTextarea();
  }
};
</script>

<style lang="stylus">
  @import '~common/stylus/variable'

    textarea&
      max-width: 100%
      height: auto
      min-height: $input-height-base
      vertical-align: bottom
      font-size: $font-size-base

    .input-wrapper
      display: inline-block
      width: 100%
      position: relative
      vertical-align: middle
      line-height: normal

      .input
        display: inline-block
        width: 100%
        height: inherit
        line-height: $line-height-base
        padding: $input-padding-vertical-base $input-padding-horizontal
        font-size: $font-size-base
        border: 1px solid $input-border-color
        box-sizing: border-box
        border-radius: $btn-border-radius
        color: $input-color
        background-color: $input-bg
        background-image: none
        position: relative
        cursor: text
        transition: border $transition-time $ease-in-out, background $transition-time $ease-in-out, box-shadow $transition-time $ease-in-out

        &:hover
          border-color: tint($input-hover-border-color, 20%)

        &:focus
          border-color: tint($input-hover-border-color, 20%)
          outline: 0
          box-shadow: 0 0 0 2px fade($input-hover-border-color, 20%)

        &[disabled],
        fieldset[disabled] &
          background-color: $input-disabled-bg
          opacity: 1
          cursor: $cursor-disabled
          color: #ccc
          &:hover
            border-color: tint($input-hover-border-color, 20%)

      .input-icon
        width: 32px
        height: $input-height-base
        line-height: $input-height-base
        font-size: 16px
        text-align: center
        color: $subsidiary-color
        position: absolute
        top: 4px
        right: 0
        z-index: 3

    .input-hide-icon .input-icon
      display: none

    .input-icon-validate
      display: none

    .input-icon-clear
      display: none

    .input-wrapper:hover
      .input-icon-clear
        display: inline-block

    .input-icon-normal + &
      padding-right: 32px

    .input-hide-icon .input-icon-normal + &
      padding-right: $input-padding-horizontal

    .input-wrapper-large .input-wrapper-icon
      font-size: 18px
      height: $input-height-large
      line-height: $input-height-large

    .input-wrapper-small .input-wrapper-icon
      width: 24px
      font-size: 14px
      height: $input-height-small
      line-height: $input-height-small

  .input-large
    font-size: $font-size-base
    padding: $input-padding-vertical-large $input-padding-horizontal
    height: $input-height-large

  .input-small
    padding: $input-padding-vertical-small $input-padding-horizontal
    height: $input-height-small
    border-radius: $btn-border-radius-small

  .input-error
    border: 1px solid $error-color
    &:hover
      border-color: $error-color
    &:focus
      border-color: $error-color
      outline: 0
      box-shadow: 0 0 0 2px fade($error-color, 20%)

  .input-group
    display: table
    width: 100%
    border-collapse: separate
    position: relative
    font-size: $font-size-small
    top: 1px

    .input-group-large
      font-size: $font-size-base

    &[class*='col-']
      float: none
      padding-left: 0
      padding-right: 0

    > [class*='col-']
      padding-right: 8px
</style>
