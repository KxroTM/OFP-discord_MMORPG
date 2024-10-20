
class inventory :
    def __init__(self, items, ) :
        self.items = items

    async def use(self, item) :
        if item in self.items :
            await item.use()
        else :
            return False