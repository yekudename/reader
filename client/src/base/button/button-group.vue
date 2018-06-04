<template>
    <div :class="classes">
        <slot></slot>
    </div>
</template>
<script>
    import { oneOf } from 'common/utils/assist'

    const prefixCls = 'btn-group'

    export default {
        name: 'ButtonGroup',
        props: {
            size: {
                validator (value) {
                    return oneOf(value, ['small', 'large', 'default'])
                }
            },
            shape: {
                validator (value) {
                    return oneOf(value, ['circle', 'circle-outline'])
                }
            },
            vertical: {
                type: Boolean,
                default: false
            }
        },
        computed: {
            classes () {
                return [
                    `${prefixCls}`,
                    {
                        [`${prefixCls}-${this.size}`]: !!this.size,
                        [`${prefixCls}-${this.shape}`]: !!this.shape,
                        [`${prefixCls}-vertical`]: this.vertical
                    }
                ]
            }
        }
    }
</script>

<style lang="stylus">
.btn-group:not(.btn-group-vertical) &:not(:first-child):not(:last-child) 
    border-right-color: $btn-group-border
    border-left-color: $btn-group-border


.btn-group:not(.btn-group-vertical) &:first-child 
    &:not(:last-child) 
        border-right-color: $btn-group-border
        &[disabled] 
            border-right-color: $btn-default-border
        
    


.btn-group:not(.btn-group-vertical) &:last-child:not(:first-child),
.btn-group:not(.btn-group-vertical) & + .btn
    border-left-color: $btn-group-border
    &[disabled]
        border-left-color: $btn-default-border
    


.btn-group-vertical &:not(:first-child):not(:last-child)
    border-top-color: $btn-group-border
    border-bottom-color: $btn-group-border


.btn-group-vertical &:first-child
    &:not(:last-child) 
        border-bottom-color: $btn-group-border
        &[disabled] 
            border-top-color: $btn-default-border
        
    


.btn-group-vertical &:last-child:not(:first-child)
.btn-group-vertical & + .btn
    border-top-color: $btn-group-border
    &[disabled] 
        border-bottom-color: $btn-default-border


.btn-group
    btn-group(btn-group)

.btn-group-vertical 
    btn-group-vertical(btn-group)
</style>
