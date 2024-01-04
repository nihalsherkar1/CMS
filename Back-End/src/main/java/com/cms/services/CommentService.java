package com.cms.services;

import com.cms.dto.CommentDto;
import com.cms.models.Comment;

public interface CommentService {
	
	public String addComment(CommentDto comment);

}
