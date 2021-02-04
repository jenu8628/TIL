<template>
  <div>
    <table class="table table-hover" style="width:100%" align="center">
      <tr v-for="comment in comments" :key="comment.comment_num">
        <td width="70%">{{ comment.comment_content }}</td>
        <td width="10%">{{ comment.comment_writer }}</td>
        <td width="10%">{{ comment.write_date }}</td>
        <td width="10%">
          <div v-if="$store.getters.getUserId == comment.comment_writer">
            <button
              class="btn btn-danger"
              @click="delComment(comment.comment_num)"
              type="button"
            >
              삭제
            </button>
          </div>
        </td>
      </tr>
      <tr
        v-if="
          this.$store.getters.getUserInfo == 1 ||
            this.$store.getters.getUserInfo == 0
        "
      >
        <td colspan="4">
          <div class="input-group mb-3">
            <textarea class="form-control" rows="3" v-model="comment" />
            <div class="input-group-append">
              <button
                class="btn btn-primary"
                @click="registComment"
                type="button"
              >
                댓글등록
              </button>
            </div>
          </div>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import axios from "@/plugins/axios";
export default {
  created() {
    axios.get("/api/comment/" + this.$route.params.bno).then(response => {
      this.comments = response.data;
    });
  },
  data() {
    return {
      comments: [],
      comment: ""
    };
  },
  methods: {
    registComment() {
      axios
        .post("/api/comment", {
          board_num: this.$route.params.bno,
          comment_content: this.comment
        })
        .then(response => {
          console.log(response);
        });
      //   this.$router.go();
      //   this.$forceUpdate();
    },
    delComment(num) {
      console.log(num);
      //   this.$router.go();
    }
  }
};
</script>

<style></style>
