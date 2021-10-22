

def plot_null_columns(df: 'DataFrame') -> None:
    """Skapar ett stapeldiagram med staplar för alla kolumner med NaN-värden"""
    import seaborn as sb

    # Kolumner med null-värden
    nullkolumner = df.columns[df.isnull().sum() > 0]
    
    # Antalet null-värden i varje kolumn
    antal_null = df[nullkolumner].isnull().sum()

    # Plotta 
    ax = sb.barplot(x= nullkolumner, y= antal_null)
    ax.set_title("Null värden" ) 
    ax.set_xlabel("Kolumn")
    ax.set_ylabel("Antal")
