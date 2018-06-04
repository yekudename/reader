<template>
  <li class="index-list-group">
    <h2 class="index-list-anchor">{{group.name}}</h2>
    <ul>
      <slot>
        <cube-index-list-item v-for="(item, index) in group.items" :key="index" :item="item" @select="selectItem"></cube-index-list-item>
      </slot>
    </ul>
  </li>
</template>

<script type="text/ecmascript-6">
import CubeIndexListItem from './index-list-item.vue'

const COMPONENT_NAME = 'index-list-group'
const EVENT_SELECT = 'select'

export default {
  name: COMPONENT_NAME,
  props: {
    group: {
      type: Object,
      default() {
        return {}
      }
    }
  },
  methods: {
    selectItem(item) {
      this.$emit(EVENT_SELECT, item)
    }
  },
  components: {
    CubeIndexListItem
  }
}
</script>
