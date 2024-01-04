package com.cms.dao;

import org.springframework.data.jpa.repository.JpaRepository;

import com.cms.models.Comment;

public interface CommentsDao extends JpaRepository<Comment, Long> {

}
