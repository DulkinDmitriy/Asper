# Api routes

## api/post [GET]
    [GET]
        Return all posts.
        
    [POST]
        Create new post.

## api/post/<id> [GET, PUT, DELETE]
    [GET]
        Return post by id.
    
    [PUT]
        Replace current post or create a new item.
    
    [DELETE]
        Delete current post
    
    Errors:
        Access denied error: 
            `{
                "error": {
                    "message" = "Access denied"
                }
            }`
        Item not found error [GET, PUT, DELETE]:
            `{
                "error": {
                    "message" = "Item not found",
                    "item_id" = <id>
                }
            }`
