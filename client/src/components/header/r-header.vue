<template>
  <div class="r-header">
    <div class="header-top">
      <div class="home">
        <i class="fa fa-home fa-lg"></i>
      </div>
      <h1 class="text">看书</h1>
      <section class="header-right">
        <router-link tag="div" to="/search" class="search">
          <div class="fa fa-search"></div>
        </router-link>
        <router-link tag="div" class="mine" to="/home/account">
          <i class="fa fa-ellipsis-h"></i>
        </router-link>
      </section>
    </div>
    <div class="header-tab">
      <tab></tab>
    </div>
  </div>
</template>

<script>
import Tab from 'components/tab/r-tab'
export default {
  components: {
    Tab
  }
}
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  @import "~common/stylus/variable"
  @import "~common/stylus/mixin"

  .r-header
    position: relative
    height: 44px
    color: $primary-color
    .header-top
      padding-left: 10px
      display: flex
      align-items: center
      .home
        vertical-align: middle
        text-align: center
        width: 30px
        line-height: 44px
        font-size: $font-size-large
      .text
        display: inline-block
        vertical-align: top
        line-height: 44px
        font-size: $font-size-large
      .header-right
        position: absolute
        display: flex
        top: 0
        right: 0
        height: 100%
        .search
          font-size: 20px
          padding: 12px
        .mine
          display: block
          padding: 12px
          font-size: 20px
          color: $primary-color
</style>