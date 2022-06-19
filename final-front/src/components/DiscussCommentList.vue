<template>
  <div class="comment-list d-flex flex-column">
    <div class="d-flex">
      <h3>댓글</h3>

    </div>
    <ul>
      <discuss-comment-list-item 
        v-for="comment in discuss.discuss_comments" 
        :comment="comment" 
        :key="comment.pk">
      </discuss-comment-list-item>        
    </ul>

    <discuss-comment-list-form></discuss-comment-list-form>
  </div>
</template>

<script>
import DiscussCommentListItem from '@/components/DiscussCommentListItem.vue'
import DiscussCommentListForm from '@/components/DiscussCommentListForm.vue'
// import { mapGetters, mapActions } from 'vuex'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'DiscussCommentList',
  components: { DiscussCommentListForm, DiscussCommentListItem },
  props: { comments: Array },
  computed: {
    ...mapGetters(['discuss']),
  },
  methods: {
    ...mapActions(['createDiscussComment']),
  }
}
</script>

<style>
.comment-list {
  /* border: 1px solid blue; */
  width: 100%;
}
ul {
  list-style:none;
  padding-left: 0 !important;
}
</style>