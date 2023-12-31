package com.cms.controller;

 
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.cms.entities.Blogs;
import com.cms.services.BlogServiceImpl;

@RestController
@RequestMapping("/cms/blog")
public class BlogController {

	@Autowired
	private BlogServiceImpl blogServiceImpl;
	
	
	@PostMapping("/addblog")
	public Blogs addBlogs( @RequestBody  Blogs blogs ){
		
		return  blogServiceImpl.addBlog(blogs);
		
	}
}
