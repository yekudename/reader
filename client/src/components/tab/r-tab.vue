<template>
  <div class="tab">
    <router-link tag="div" class="tab-item" to="/home/bookshelf">
      <span class="tab-link">书架</span>
    </router-link>
    <router-link tag="div" class="tab-item" to="/home/discover">
      <span class="tab-link">发现
      </span>
    </router-link>
    <router-link tag="div" class="tab-item" to="/home/account">
      <span class="tab-link">账户</span>
    </router-link>
  </div>
</template>

<style scoped lang="stylus" rel="stylesheet/stylus">
  @import "~common/stylus/variable"
  .tab
    position: relative
    display: flex
    height: 44px
    line-height: 44px
    font-size: $fontsize-medium
    background: $color-background
    .tab-item
      flex: 1
      text-align: center
      margin-right: 2px
      .tab-link
        padding: 0 10px 5px 10px
        color: $color-grey
      &.router-link-active
        .tab-link
          color: $primary-color
          border-bottom: 2px solid $primary-color
</style>
