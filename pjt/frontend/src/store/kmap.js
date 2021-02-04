import store from "../store";

const state = {
  gu: "",
  dong: "",
  buildsel: 0,
  search: "",
  flag: 1
};

const getters = {
  getGu: state => state.gu,
  getDong: state => state.dong,
  getBuildSel: state => state.buildsel,
  getSearch: state => state.search,
  getFlag: state => state.flag
};

const mutations = {
  CLICK_SEARCH(state, data) {
    state.gu = data["gu"];
    state.dong = data["dong"];
    state.buildsel = data["buildsel"];
    state.search = data["search"];
  },
  CHANGE_FLAG(state) {
    state.flag *= -1;
  }
};

const actions = {
  click_search(commit, data) {
    store.commit("CLICK_SEARCH", data);
  },
  change_flag() {
    store.commit("CHANGE_FLAG");
  }
};

export default {
  state: {
    ...state
  },
  getters,
  mutations,
  actions
};
