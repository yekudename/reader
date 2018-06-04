<template>
  <div class="home">
    <div class="home-header">
      <r-header></r-header>
      <r-tab></r-tab>
    </div>
    <div class="home-content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import RTab from 'components/tab/r-tab'
import RHeader from 'components/header/r-header'

export default {
  name: 'home',
  components: {
    RTab,
    RHeader
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .home
    width: 100%
    height: 100%
    overflow: hidden
    .home-header
      width: 100%
    .home-content
      width: 100%
      height: calc(100% - 88px)
      overflow: hidden
</style>
