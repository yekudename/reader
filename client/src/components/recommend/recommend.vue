<template>
  <div class="recommend" ref="recommend">
    <list :title="title">
      <div class="recommend-list">
        <li class="recommend-item" v-for="(item, index) in recommends" :key="index" @click="handleSelect(item)">
          <slot>
            <img :src="item.img" class="recommend-item-img">
            <div class="recommend-item-name">{{item.name}}</div>
          </slot>
        </li>
      </div>    
    </list>
  </div>
</template>

<script>
import List from 'components/comment/list'

export default {
  props: {
    title: String,
    recommends: [Object, Array]
  },
  methods: {
    handleSelect(item) {
      this.$emit('select', item)
    }
  },
  components: {
    List
  }
}
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  @import "~common/stylus/variable"

  .recommend
    padding: 0
    .recommend-list
      display: flex
      padding-top: 10px
      .recommend-item
        width: inherit
        display: flex
        flex-direction: column
        flex: 1
        overflow: hidden
        .recommend-item-img,.recommend-item-name
          align-self: center
        .recommend-item-img
          width: 70px
          height: 90px
        .recommend-item-name
          padding-top: 5px
          width: 70px
          text-align: center
          font-size: $fontsize-medium
          word-wrap: break-word
          white-space: nowrap
          overflow: hidden
          text-overflow: ellipsis
</style>
