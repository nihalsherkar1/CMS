package com.cms.services;

import java.util.Map;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.cms.entities.Blogs;
import com.cms.entities.Users;
import com.cms.repository.BlogRepository;

@Service
public class BlogServiceImpl implements BlogService{

	@Autowired(required = true)
	  private BlogRepository blogRepository;
	
	@Autowired(required = true)
	private Users users;
	
	@Autowired(required = true)
	private UserServiceImpl userServiceImpl;

	@Autowired(required = true)
	private Blogs blogs;
	
	
	public Blogs addBlog(Blogs blogs ) {
		 
			
			 return  blogRepository.save(blogs);
		  
	}
	
 

	
	
}
