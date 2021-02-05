import store from "../store";

const state = {
  acc_token: "",
  ref_token: ""
};

const getters = {
  getAccToken: state => state.acc_token,
  getRefToken: state => state.ref_token
};

const mutations = {
  UPDATE_TOKEN(state, token) {
    state.acc_token = token[0];
    state.ref_token = token[1];
  },
  LOGOUT_TOKEN(state) {
    state.acc_token = "";
    state.ref_token = "";
  }
};

const actions = {
  update_token(commit, token) {
    store.commit("UPDATE_TOKEN", token);
  },
  logout_token() {
    store.commit("LOGOUT_TOKEN");
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
