package com.cms.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.cms.dto.BlogDto;
import com.cms.models.Blog;
import com.cms.services.BlogService;


@CrossOrigin("*")
@RestController
@RequestMapping("/cms/blogs")
public class BlogsController {
	
	@Autowired
	private BlogService bser;
	
	@PostMapping("/add")
	public String addBlog(BlogDto blog) {
		return bser.saveBlog(blog);
	}
	
	@GetMapping("/displayAllBlogs")
	public List<Blog> displayAll(){
		
		return bser.showBlogs();
	}
	
}
