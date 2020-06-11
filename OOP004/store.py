import re
total_items=[]
total_items_list=""
class Item():
    def __init__(self,name, price, category):
        self.name=name
        self.cost(price)
        self.category=category

    def cost(self,price):
        if price>0:
            self.price=price
        else:
            raise ValueError(f"Invalid value for price, got {price}")


    def __str__(self):
        return f"{self.name}@{self.price}-{self.category}"


class Query(Item):
    def __init__(self,field, operation, value):
        self.field=field
        self.operation=operation
        self.value=value

    def __str__(self):
        return f"{self.field} {self.operation} {self.value}"

class Store(Query):
     def __init__(self,outputs=None):
         self.total_items=[]
         self.total_items_list=""
         self.question=""
         self.lists=[]
         self.dictionary={}
         self.output=[]
         self.final=""
         self.usha=outputs

     def add_item(self,item):
         self.total_items.append(str(item))
         self.dictionary["name"]=item.name
         self.dictionary["price"]=item.price
         self.dictionary["category"]=item.category
         self.dictionary["combine"]=f"{item.name}@{item.price}-{item.category}"
         self.lists.append(self.dictionary)
         self.dictionary={}

     def __str__(self):
         if not self.usha:
            for i in range(len(self.total_items)):
                if i!=(len(self.total_items)-1):
                    self.total_items_list=self.total_items_list+self.total_items[i]+"\n"
                else:
                    self.total_items_list=self.total_items_list+self.total_items[i]
            return f"{self.total_items_list}"
         else:
            return "\n".join(self.usha)


     def filter(self,query):
         if query.operation=="EQ":
             for i in self.lists:
                 if i[query.field]==query.value:
                     self.output.append(i["combine"])
             if not self.output:
                 self.output.append("No items")
             return (Store(self.output))

         elif query.operation=="GT":
             for i in self.lists:
                 if i[query.field]>query.value:
                     self.output.append(i["combine"])
             if not self.output:
                 self.output.append("No items")
             return (Store(self.output))

         elif query.operation=="LT":
             for i in self.lists:
                 if i[query.field]<query.value:
                     self.output.append(i["combine"])
             if not self.output:
                 self.output.append("No items")
             return (Store(self.output))

         elif query.operation=="GTE":
             for i in self.lists:
                 if i[query.field]>=query.value:
                     self.output.append(i["combine"])
             if not self.output:
                 self.output.append("No items")
             return (Store(self.output))

         elif query.operation=="LTE":
             for i in self.lists:
                 if i[query.field]<=query.value:
                     self.output.append(i["combine"])
             if not self.output:
                 self.output.append("No items")
             return (Store(self.output))

         elif query.operation=="STARTS_WITH":
             for i in self.lists:
                 if i[query.field].startswith(query.value):
                     self.output.append(i["combine"])
             if not self.output:
                 self.output.append("No items")
             return (Store(self.output))

         elif query.operation=="ENDS_WITH":
             for i in self.lists:
                 if i[query.field].endswith(query.value):
                     self.output.append(i["combine"])
             if not self.output:
                 self.output.append("No items")
             return (Store(self.output))

         elif query.operation=="CONTAINS":
             for i in self.lists:
                 if (query.value) in i[query.field]:
                     self.output.append(i["combine"])
             if not self.output:
                 self.output.append("No items")
             return (Store(self.output))

         elif query.operation=="IN":
             for i in self.lists:
                 for j in query.value:
                    if j in i[query.field]:
                        self.output.append(i["combine"])
             if not self.output:
                 self.output.append("No items")
             return (Store(self.output))
         else:
             raise ValueError("Invalid value for operation, got random")



     def exclude(self,query):
         if query.operation=="EQ":
             for i in self.lists:
                 if i[query.field]!=query.value:
                     self.output.append(i["combine"])
             if not self.output:
                 self.output.append("No items")
             return (Store(self.output))

         elif query.operation=="GT":
             for i in self.lists:
                 if i[query.field]<=query.value:
                     self.output.append(i["combine"])
             if not self.output:
                 self.output.append("No items")
             return (Store(self.output))

         elif query.operation=="LT":
             for i in self.lists:
                 if i[query.field]>=query.value:
                     self.output.append(i["combine"])
             if not self.output:
                 self.output.append("No items")
             return (Store(self.output))

         elif query.operation=="GTE":
             for i in self.lists:
                 if i[query.field]<query.value:
                     self.output.append(i["combine"])
             if not self.output:
                 self.output.append("No items")
             return (Store(self.output))

         elif query.operation=="LTE":
             for i in self.lists:
                 if i[query.field]>query.value:
                     self.output.append(i["combine"])
             if not self.output:
                 self.output.append("No items")
             return (Store(self.output))

         elif query.operation=="STARTS_WITH":
             for i in self.lists:
                 if not i[query.field].startswith(query.value):
                     self.output.append(i["combine"])
             if not self.output:
                 self.output.append("No items")
             return (Store(self.output))

         elif query.operation=="ENDS_WITH":
             for i in self.lists:
                 if not i[query.field].endswith(query.value):
                     self.output.append(i["combine"])
             if not self.output:
                 self.output.append("No items")
             return (Store(self.output))

         elif query.operation=="CONTAINS":
             for i in self.lists:
                 if  (query.value) not in i[query.field]:
                     self.output.append(i["combine"])
             if not self.output:
                 self.output.append("No items")
             return (Store(self.output))

         elif query.operation=="IN":
             for i in self.lists:
                 for j in query.value:
                    if j not in i[query.field]:
                        self.output.append(i["combine"])
             if not self.output:
                 self.output.append("No items")
             return (Store(self.output))

         else:
             raise ValueError("Invalid value for operation, got random")












store = Store()
item = Item(name="Oreo Biscuits", price=30, category="Food")
store.add_item(item)
item = Item(name="Boost Biscuits", price=20, category="Food")
store.add_item(item)
item = Item(name="ParleG Biscuits", price=10, category="Food")
store.add_item(item)
query = Query(field="price", operation="GT", value=15)
results = store.exclude(query)
print(results)
new_result=results.exclude(query)
print(new_result)