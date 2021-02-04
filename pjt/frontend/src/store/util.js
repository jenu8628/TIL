import store from "../store";

const state = {
  savePath: "",
  searchTitle: "",
  searchPage: 1
};

const getters = {
  getSavePath: state => state.savePath,
  getSearchTitle: state => state.searchTitle,
  getSearchPage: state => state.searchPage
};

const mutations = {
  UPDATE_SAVEPATH(state, path) {
    state.savePath = path;
  },
  UPDATE_SEARCHDATA(state, data) {
    state.searchTitle = data["search"];
    state.searchPage = data["page"];
  },
  DELETE_SEARCHDATA() {
    state.searchTitle = null;
    state.searchPage = 1;
  }
};

const actions = {
  update_savepath(commit, path) {
    store.commit("UPDATE_SAVEPATH", path);
  },
  update_searchdata(commit, data) {
    store.commit("UPDATE_SEARCHDATA", data);
  },
  delete_searchdata() {
    store.commit("DELETE_SEARCHDATA");
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
