from pyspark.sql import SparkSession, DataFrame

spark = SparkSession.builder.appName("pyspark_test").getOrCreate()

categories = spark.createDataFrame([
    (1, "Category 1"),
    (2, "Category 2"),
    (3, "Category 3"),
    (4, "Category 4"),
    (5, "Category 5"),
    ["id", "category"],
])

products = spark.createDataFrame([
    (1, "Product 1"),
    (2, "Product 2"),
    (3, "Product 3"),
    (4, "Product 4"),
    (5, "Product 5"),
    (6, "Product 6"),
    (7, "Product 7"),
    (8, "Product 8"),
    (9, "Product 9"),
    (10, "Product 10"), ],
    ["id", "product", ]
)

data = spark.createDataFrame([
    (4, 5),
    (5, 6),
    (3, 4),
    (2, 3),
    (3, 2),
    (4, 2),
    (1, 1),
    (1, 8),
    (4, 9),
    (5, 10),
    (5, 3),],
    ["category_id", "product_id", ]
)

df_data = (products.join(data, products.id == data.product_id, how='left').join(categories,data.category_id == categories.id, how='left').select(['category', 'product']))

df_data.orderBy("category_id", "product_id").show(truncate=True)