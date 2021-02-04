<template>
  <div>
    <b-form-input
      id="title"
      size="lg"
      style="margin-bottom:50px"
      v-model="board_title"
    ></b-form-input>
    <b-form-textarea
      id="textarea"
      style="margin-bottom:50px"
      v-model="board_content"
      rows="15"
      size="lg"
      max-rows="15"
    ></b-form-textarea>
    <button @click="modify" class="btn btn-primary mb-5">
      글수정
    </button>
  </div>
</template>

<script>
import axios from "@/plugins/axios";
export default {
  created() {
    axios.get("/api/board/" + this.$route.params.nno).then(response => {
      this.board_title = response.data["board_title"];
      this.board_content = response.data["board_content"];
    });
  },
  data() {
    return {
      board_title: "",
      board_content: ""
    };
  },
  methods: {
    modify() {
      axios
        .put("/api/board/" + this.$route.params.nno, {
          board_title: this.board_title,
          board_content: this.board_content
        })
        .then(response => {
          if (response.status == 200) {
            alert("정상적으로 수정되었습니다.");
            this.$router.push("/board/" + this.$route.params.nno);
          } else {
            alert("수정에 실패하였습니다.");
          }
        });
    }
  }
};
</script>

<style></style>
