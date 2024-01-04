package com.cms.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.cms.dto.CommentDto;
import com.cms.models.Comment;
import com.cms.services.CommentService;

@RestController
@RequestMapping("/cms/comments")
@CrossOrigin("*")
public class CommentsController {
	
	@Autowired
	private CommentService cser;
	
	@PostMapping("/post")
	public String postComment(@RequestBody CommentDto comment) {
		
		return cser.addComment(comment);
	}

}
