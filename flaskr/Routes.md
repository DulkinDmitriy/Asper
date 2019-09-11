# Api routes

## api/post/getAll [GET]
        Return all posts.

        with_likes? - Include likes in response;
        with_comments? - Include comments in response;
        count - count of posts;

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
    
## api/post/create [POST]    
        Create new post.
        
        `{
            "title": <post_title>,
            "image": <post_image>,
            "content": <post_content>
        }`

        Errors:
            Access Denied Error: 
                `{
                    "message": "Access denied",
                    "details": "User should be authorized for creating new post"
                }`

## api/post/get [GET]
        Return post by id.

        id - primary key for searching;
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

        Item not found error:
            `{
                "error": {
                    "message" = "Item not found",
                    "details" = "Collection has no contain item with this id",
                    "item_id" = <id>
                }
            }`

## api/post/update [PUT]
    Update current post.

        id - primary key for searching;

        `{
            "title": <post_title>,
            "image": <post_image_path>,
            "content": <post_content>
        }`

        Errors:
        Access denied error: 
            `{
                "error": {
                    "message" = "Access denied",
                    "details" = "User should be author or administrator." 
                }
            }`

        Item not found error:
            `{
                "error": {
                    "message" = "Item not found",
                    "details" = "Collection has no contain item with this id",
                    "item_id" = <id>
                }
            }`

## api/post/delete [DELETE]
    Delete post by id.

    id - primary key for searching;

    Errors:
        Access denied error: 
            `{
                "error": {
                    "message" = "Access denied",
                    "details" = "User should be author or administrator." 
                }
            }`

        Item not found error:
            `{
                "error": {
                    "message" = "Item not found",
                    "details" = "Collection has no contain item with this id",
                    "item_id" = <id>
                }
            }`

## /api/comment/getAll [GET]
    Return all comments.

        with_likes? - Include likes in response;

        `{
            "comments": [
                {
                    "id": <commnet_id>,
                    "author": <comment_author>,
                    "content": <comment_content>,
                    "createdTimestamp": <comment_datetime>,
                    "edited": <comment_bool>,
                    "likes_count": <likes_count>,
                    "likes": [
                        ...
                    ]
                },
                ...
            ]
        }`

## /api/comment/create [POST]
    Create new commnet to post.

        id - Post primary key.

        `{
            "author": <comment_author>,
            "content": <comment_content>
        }`

## /api/comment/update [PUT]
    Update current comment

        id - Primary key for searching item.

        `{
            "author": <comment_author>,
            "content": <comment_content>
        }`

        Errors:
        Access denied error: 
            `{
                "error": {
                    "message" = "Access denied",
                    "details" = "User should be author or administrator." 
                }
            }`

        Item not found error:
            `{
                "error": {
                    "message" = "Item not found",
                    "details" = "Collection has no contain item with this id",
                    "item_id" = <id>
                }
            }`

## /api/comment/delete [DELETE]
    Delete current comment

        id - Primary key for searching item.

        Errors:
        Access denied error: 
            `{
                "error": {
                    "message" = "Access denied",
                    "details" = "User should be author or administrator." 
                }
            }`

        Item not found error:
            `{
                "error": {
                    "message" = "Item not found",
                    "details" = "Collection has no contain item with this id",
                    "item_id" = <id>
                }
            }`

## /api/comment/like [POST]
    Increment like count to comment

        id - Primary key for searching item.

        `{
            "owner": <like_owner>
        }`

        Error: 
            Like was placed.
                `{
                    "message": "Wrong behavior.",
                    "details": "User has like this comment.",
                    "item_id": <id>
                }`

## /api/comment/dislike [DELETE]
    Decrement like count to comment

        id - Primary key for searching item.

        Error: 
            Like wasn`t placed.
                `{
                    "message": "Wrong behavior.",
                    "details": "User has no likes on this comment.",
                    "item_id": <id>
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
