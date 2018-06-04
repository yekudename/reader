<template>
  <div>
    <div>
      <c-menu mode="horizontal" theme="primary">
        <submenu name="3" width="100%">
          <template slot="title">统计分析</template>
          <menu-item name="3-1">新增和启动</menu-item>
          <menu-item name="3-1">活跃分析</menu-item>
        </submenu>
        <menu-item name="4">活跃分析</menu-item>
        <menu-item name="5">活跃分析</menu-item>
      </c-menu>
    </div>
    <div>
    <dropdown trigger="click" style="margin-top:10px">
      <a>下拉菜单</a>
      <drop-menu slot="list">
        <dropdown-item>驴打滚</dropdown-item>
        <dropdown-item>炸酱面</dropdown-item>
        <dropdown-item>豆汁儿</dropdown-item>
        <dropdown-item>冰糖葫芦</dropdown-item>
      </drop-menu>
    </dropdown>
    </div>
  </div>
</template>

<script>
import CMenu from 'components/menu/menu'
import MenuItem from 'components/menu/menu-item'
import Submenu from 'components/menu/submenu'
import Dropdown from 'base/dropdown/dropdown'
import DropMenu from 'base/dropdown/dropdown-menu'
import DropdownItem from 'base/dropdown/dropdown-item'
export default {
  components: {
    CMenu,
    MenuItem,
    Submenu,
    Dropdown,
    DropMenu,
    DropdownItem
  },
  methods: {
    handleItemSelect() {
      console.log(123)
    }
  },
  created() {
    console.log(this.$parent.$options.name)
  }
}
</script>