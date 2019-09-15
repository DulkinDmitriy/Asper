# Api routes

##  /api/getAllPosts [GET]
        Return all posts.

        Request: 
            "with_likes": ...,
            "with_comments": ...,
            "count": ... 
            

        with_likes? - Include likes in response;
        with_comments? - Include comments in response;
        count - count of posts;

        Response:
            `{
                "posts": [
                    {
                        "id": <post_id>,
                        "title": <post_title>,
                        "image": <post_image_path>,
                        "content": <post_con    tent>,
                        "created_datetime": <comment_datetime>,
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
    
## api/createPost [POST]    
        Create new post.
        
        Request:

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


## api/getPost [GET]
        Return post by id.


        with_likes? - Include likes in response;
        with_comments? - Include comments in response;

        `{
            "id": <post_id>,
            "title": <post_title>,
            "image": <post_image_path>,
            "content": <post_content>,
            "created_datetime": <comment_datetime>,
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

## api/updatePost [PUT]
    Update current post.

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

## api/deletePost [DELETE]
    Delete post by id.

        `{
            "post_id": <id>
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

## /api/getAllComments [GET]
    Return all comments.

        with_likes? - Include likes in response;

        `{
            with_likes: ...
        }`

        `{
            "comments": [
                {
                    "id": <commnet_id>,
                    "author": <comment_author>,
                    "content": <comment_content>,
                    "created_datetime": <comment_datetime>,
                    "edited": <comment_bool>,
                    "likes_count": <likes_count>,
                    "likes": [
                        ...
                    ]
                },
                ...
            ]
        }`

## /api/createComment [POST]
    Create new commnet to post.

        `{
            "post_id": ...
            "author": <comment_author>,
            "content": <comment_content>
        }`

## /api/updateComment [PUT]
    Update current comment

        `{
            "comment_id": ...
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

## /api/deleteComment [DELETE]
    Delete current comment

        '{
            "comment_id": ...
        }'

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

## /api/putLikeToPost [POST]
    Increment like count to post

        `{
            "post_id": <comment_id>,
            "owner": <like_owner>
        }`

    Error: 
        Like was placed.
            `{
                "message": "Wrong behavior.",
                "details": "User has like this post.",
                "item_id": <id>
            }`

## /api/deleteLikeFromPost [DELETE]
    Decrement like count to post

        `{
            "post_id": ...
        }`

        Error: 
            Like wasn`t placed.
                `{
                    "message": "Wrong behavior.",
                    "details": "User has no likes on this post.",
                    "item_id": <id>
                }`

## /api/putLikeToComment [POST]
    Increment like count to comment

        `{
            "comment_id": <comment_id>,
            "owner": <like_owner>
        }`

        Error: 
            Like was placed.
                `{
                    "message": "Wrong behavior.",
                    "details": "User has like this comment.",
                    "item_id": <id>
                }`

## /api/deleteLikeFromComment [DELETE]
    Decrement like count to comment

        `{
            "comment_id": ...
        }`

        Error: 
            Like wasn`t placed.
                `{
                    "message": "Wrong behavior.",
                    "details": "User has no likes on this comment.",
                    "item_id": <id>
                }`