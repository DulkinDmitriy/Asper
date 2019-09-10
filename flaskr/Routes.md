# Api routes

## api/posts [GET]
    [GET]
        Return all posts.

        with_likes? - Include likes in response;
        with_comments? - Include comments in response;
        counts - counts of posts;

        `{
            "posts": [
                {
                    "id": <post_id>,
                    "title": <post_title>,
                    "image": <post_image_path>,
                    "content": <post_content>,
                    "comments_count": <comments_count>,
                    "likes_count": <likes_count>,


                    "comments": [
                        ...
                    ],

                    "likes": [
                        ...
                    ]
                },
                ...
            ]
        }`
    
## api/post [POST]    
    [POST]
        Create new post.

        `{
            "title": <post_title>,
            "image": <post_image_path>,
            "content": <post_content>
        }`

        Errors:
            Access Denied Error: 

                `{
                    "message": "Access denied",
                    "details": "User should be authorized for creating new post"
                }`

## api/post?p=<int:post_id> [GET, PUT, DELETE]
    [GET]
        Return post by id.

        with_likes? - Include likes in response;
        with_comments? - Include comments in response;

        `{
            "id": <post_id>,
            "title": <post_title>,
            "image": <post_image_path>,
            "content": <post_content>,
            "comments_count": <comments_count>,
            "likes_count": <likes_count>,


            "comments": [
                ...
            ],

            "likes": [
                ...
            ]
        }`
    
    [PUT]
        Replace current post or create a new item.

        `{
            "title": <post_title>,
            "image": <post_image_path>,
            "content": <post_content>
        }`
    
    [DELETE]
        Delete current post
    
    Errors:
        Access denied error [PUT, DELETE]: 
            `{
                "error": {
                    "message" = "Access denied",
                    "details" = "User should be author or administrator." 
                }
            }`

        Item not found error [GET, DELETE]:
            `{
                "error": {
                    "message" = "Item not found",
                    "item_id" = <id>
                }
            }`

## /api/comments [GET]
    [GET]
        Return all comments.

        with_likes? - Include likes in response;

        `{
            "comments": [
                {
                    "id": <commnet_id>,
                    "author": <comment_author>,
                    "content": <comment_content>,
                    "likes_count": <likes_count>,
                    "likes": [
                        ...
                    ]
                },
                ...
            ]
        }`

## /api/comments?p=<int:post_id> [GET, DELETE]
    [GET]
        Return all comments to post.
        
        - with_likes? - Include likes in response;

        `{
            "post_id": <post_id>
            "comments": [
                {
                    "id": <commnet_id>,
                    "author": <comment_author>,
                    "content": <comment_content>,
                    "likes_count": <likes_count>,
                    "likes": [
                        ...
                    ]
                },
                ...
            ]
        }`

    [DELETE]
        Delete all comments from post.

        `{
            "post_id": <post_id>
        }`

    Errors:
        Item not found error:
            
            `{
                "message": "Item not found",
                "details": "Post not found",
                "item_id": <item_id>
            }`

## /api/comment?p=<int:post_id> [POST, PUT, DELETE]
    [POST]
        Create comment to post.
        
        `{
            "author": <comment_author>
            "content": <comment_content>,
        }`

    [PUT]
        Update comment to post.

        `{
            "author": <comment_autor>,
            "content": <comment_content>
        }`

    [DELETE]
        Delete comment from post.
        
## /api/posts/likes?p=<int:post_id> [POST, DELETE]
    [POST]
        Create like to post.

    [DELETE]
        Delete like from post.

        Error: 
            Like wasn`t placed.
                `{
                    "message": "Wrong behavior.",
                    "details": "User has no likes."
                }`

        