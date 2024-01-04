package com.cms.services;

import java.util.List;

import com.cms.dto.BlogDto;
import com.cms.models.Blog;


public interface BlogService {
	
	/*  Method to save blog in database    */
	public String saveBlog(BlogDto blog);
	
	/*  Show no of blogs */
	public List<Blog> showBlogs();
}
